from django.shortcuts import render, redirect
from django.views.generic import ListView, DeleteView, UpdateView, DetailView, CreateView
from .models import Post, Comment, Category
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q

class PostListView(ListView):
    model = Post
    
    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q', '')
        if q:
            qs = qs.filter(Q(title__icontains=q)|Q(content__icontains=q)|Q(comment__content__icontains=q)|Q(user__nickname__icontains=q)).distinct()
        return qs
    
post_list = PostListView.as_view()

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/form.html'
    
    def form_valid(self, form):
        mypost = form.save(commit=False)
        mypost.user = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('blog:post_detail', kwargs={'pk': self.object.pk})
    
create_post = PostCreateView.as_view()

class PostDetailView(DetailView):
    model = Post
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context
    
    def get_object(self, queryset=None):
        pk = self.kwargs['pk']
        post = Post.objects.get(pk=pk)
        post.views += 1
        post.save()
        return super().get_object(queryset)
    
post_detail = PostDetailView.as_view()

class PostEditView(UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/form.html'
    
    def get_success_url(self):
        return reverse_lazy('blog:post_detail', kwargs={'pk': self.object.pk})
    
    def test_func(self):
        return self.get_object().user == self.request.user
    
edit_post = PostEditView.as_view()

class PostDeleteView(UserPassesTestMixin, DeleteView):
    model = Post
    
    def get_success_url(self):
        return reverse_lazy('blog:post_list')
    
    def test_func(self):
        return self.get_object().user == self.request.user
    
delete_post = PostDeleteView.as_view()

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    
    def form_valid(self, form):
        pk = self.kwargs['pk']
        post = Post.objects.get(pk=pk)
        comment = form.save(commit=False)
        comment.user = self.request.user
        comment.post = post
        comment.save()
        return redirect('blog:post_detail', pk=pk)
    
create_comment = CommentCreateView.as_view()

class CommentEditView(UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/form.html'
    
    def get_success_url(self):
        return reverse_lazy('blog:post_detail', kwargs={'pk': self.object.post.pk})
    
    def test_func(self):
        return self.get_object().user == self.request.user
    
edit_comment = CommentEditView.as_view()

class ReplyCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/form.html'
    
    def form_valid(self, form):
        pk = self.kwargs['pk']
        post = Comment.objects.get(pk=pk).post
        postpk = post.pk
        comment = form.save(commit=False)
        comment.user = self.request.user
        comment.post = post
        comment.parent_comment = Comment.objects.get(pk=pk)
        if Comment.objects.get(pk=pk).parent_comment:
            comment.parent_comment = Comment.objects.get(pk=pk).parent_comment
        comment.save()
        return redirect('blog:post_detail', pk=postpk)
    
create_reply = ReplyCreateView.as_view()