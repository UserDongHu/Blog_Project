from django import forms
from .models import Post, Comment, Category

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['category', 'title', 'content', 'thumb_image', 'file_upload', 'product_name', 'product_price', 'product_mall', 'product_link']
        widgets = {
            'category': forms.Select(
                attrs={"class": "form-control",}
            )
        }
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']