from django.db import models
from django.conf import settings

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    thumb_image = models.ImageField(
        upload_to='blog/thumb_images/%Y/%m/%d/', blank=True
    )
    file_upload = models.FileField(
        upload_to='blog/files/%Y/%m/%d/', blank=True
    )
    product_name = models.CharField(max_length=40)
    product_price = models.IntegerField()
    product_mall = models.CharField(max_length=40)
    product_link = models.TextField()
    views = models.IntegerField(default=0)
    hits = models.IntegerField(default=0)
    unhits = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    hit_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='hit_posts')
    unhit_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='unhit_posts')
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
class Category(models.Model):
    title = models.CharField(max_length=20)
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    content = models.TextField()
    hits = models.IntegerField(default=0)
    unhits = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    hit_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='hit_comments')
    unhit_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='unhit_comments')
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    
    def __str__(self):
        return self.content