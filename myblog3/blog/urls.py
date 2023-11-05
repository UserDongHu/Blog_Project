from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('mypost/', views.mypost_list, name='mypost_list'),
    path('mycomment/', views.mycomment_list, name='mycomment_list'),
    path('myhits/', views.myhits_list, name='myhits_list'),
    path('create/', views.create_post, name='create_post'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('<int:pk>/edit/', views.edit_post, name="edit_post"),
    path('<int:pk>/delete/', views.delete_post, name="delete_post"),
    path('comment/create/<int:pk>/', views.create_comment, name="create_comment"),
    path('comment/edit/<int:pk>/', views.edit_comment, name="edit_comment"),
    path('reply/create/<int:pk>/', views.create_reply, name="create_reply"),
    path('hits/post/<int:pk>/', views.hits_post, name='hits_post'),
    path('unhits/post/<int:pk>/', views.unhits_post, name='unhits_post'),
    path('hits/comment/<int:pk>/', views.hits_comment, name='hits_comment'),
    path('unhits/comment/<int:pk>/', views.unhits_comment, name='unhits_comment'),
]