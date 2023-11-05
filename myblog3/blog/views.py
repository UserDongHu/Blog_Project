from django.shortcuts import render, redirect
from django.views.generic import ListView, DeleteView, UpdateView, DetailView, CreateView
from .models import Post, Comment, Category
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.views import View
from math import ceil

class PostListView(ListView):
    model = Post
    
    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q', '')
        category = self.request.GET.get('category', '')
        if q:
            qs = qs.filter(Q(title__icontains=q)|Q(content__icontains=q)|Q(comment__content__icontains=q)|Q(user__nickname__icontains=q)).distinct()
        if category:
            qs = qs.filter(category__title=category)
        return qs
    
post_list = PostListView.as_view()

class MyPostListView(LoginRequiredMixin, ListView):
    model = Post
    
    def get_queryset(self):
        qs = super().get_queryset()
        current_user = self.request.user
        q = self.request.GET.get('q', '')
        if q:
            qs = qs.filter(Q(title__icontains=q)|Q(content__icontains=q)|Q(comment__content__icontains=q)|Q(user__nickname__icontains=q)).distinct()
        return qs.filter(user=current_user)
    
mypost_list = MyPostListView.as_view()

class MyCommentListView(LoginRequiredMixin, ListView):
    model = Post
    
    def get_queryset(self):
        qs = super().get_queryset()
        current_user = self.request.user
        q = self.request.GET.get('q', '')
        if q:
            qs = qs.filter(Q(title__icontains=q)|Q(content__icontains=q)|Q(comment__content__icontains=q)|Q(user__nickname__icontains=q)).distinct()
        return qs.filter(comment__user=current_user).distinct()
    
mycomment_list = MyCommentListView.as_view()

class MyHitsListView(LoginRequiredMixin, ListView):
    model = Post
    
    def get_queryset(self):
        qs = super().get_queryset()
        current_user = self.request.user
        q = self.request.GET.get('q', '')
        if q:
            qs = qs.filter(Q(title__icontains=q)|Q(content__icontains=q)|Q(comment__content__icontains=q)|Q(user__nickname__icontains=q)).distinct()
        return qs.filter(hit_users__in=[current_user])
    
myhits_list = MyHitsListView.as_view()

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/postform.html'
    
    def form_valid(self, form):
        mypost = form.save(commit=False)
        mypost.user = self.request.user
        user = self.request.user
        user.posting_num += 1
        user.save()
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
    template_name = 'blog/postform.html'
    
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
    template_name = 'blog/commentform.html'
    
    def form_valid(self, form):
        pk = self.kwargs['pk']
        post = Post.objects.get(pk=pk)
        comment = form.save(commit=False)
        user = self.request.user
        comment.user = user
        comment.post = post
        user.reply_num += 1
        user.save()
        comment.save()
        return redirect('blog:post_detail', pk=pk)
    
create_comment = CommentCreateView.as_view()

class CommentEditView(UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/commentform.html'
    
    def get_success_url(self):
        return reverse_lazy('blog:post_detail', kwargs={'pk': self.object.post.pk})
    
    def test_func(self):
        return self.get_object().user == self.request.user
    
edit_comment = CommentEditView.as_view()

class ReplyCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/commentform.html'
    
    def form_valid(self, form):
        pk = self.kwargs['pk']
        post = Comment.objects.get(pk=pk).post
        postpk = post.pk
        comment = form.save(commit=False)
        user = self.request.user
        comment.user = user
        comment.post = post
        user.reply_num += 1
        user.save()
        comment.parent_comment = Comment.objects.get(pk=pk)
        if Comment.objects.get(pk=pk).parent_comment:
            comment.parent_comment = Comment.objects.get(pk=pk).parent_comment
        comment.save()
        return redirect('blog:post_detail', pk=postpk)
    
create_reply = ReplyCreateView.as_view()

class HitsPostView(View):
    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        if request.user not in post.hit_users.all():
            post.hit_users.add(request.user)
            post.hits += 1
            request.user.hit_num += 1
            post.save()
            request.user.save()
        else:
            post.hit_users.remove(request.user)
            post.hits -= 1
            request.user.hit_num -=1
            post.save()
            request.user.save()
        return redirect('blog:post_detail', pk=pk)
    
hits_post = HitsPostView.as_view()

class UnHitsPostView(View):
    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        if request.user not in post.unhit_users.all():
            post.unhit_users.add(request.user)
            post.unhits += 1
            post.save()
        else:
            post.unhit_users.remove(request.user)
            post.unhits -= 1
            post.save()
        return redirect('blog:post_detail', pk=pk)
    
unhits_post = UnHitsPostView.as_view()

class HitsCommentView(View):
    def get(self, request, pk):
        comment = Comment.objects.get(pk=pk)
        if request.user not in comment.hit_users.all():
            comment.hit_users.add(request.user)
            comment.hits += 1
            comment.save()
        else:
            comment.hit_users.remove(request.user)
            comment.hits -= 1
            comment.save()
        postpk = comment.post.pk
        return redirect('blog:post_detail', pk=postpk)
    
hits_comment = HitsCommentView.as_view()

class UnHitsCommentView(View):
    def get(self, request, pk):
        comment = Comment.objects.get(pk=pk)
        if request.user not in comment.unhit_users.all():
            comment.unhit_users.add(request.user)
            comment.unhits += 1
            comment.save()
        else:
            comment.unhit_users.remove(request.user)
            comment.unhits -= 1
            comment.save()
        postpk = comment.post.pk
        return redirect('blog:post_detail', pk=postpk)
    
unhits_comment = UnHitsCommentView.as_view()
