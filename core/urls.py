from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # Articles
    path('articles/', views.article_list, name='article_list'),
    path('articles/<slug:slug>/', views.article_detail, name='article_detail'),

    # Devotionals
    path('devotionals/', views.devotional_list, name='devotional_list'),
    path('devotionals/<slug:slug>/', views.devotional_detail, name='devotional_detail'),

    # Music
    path('music/', views.music_list, name='music_list'),
    path('music/<slug:slug>/', views.music_detail, name='music_detail'),

    # Videos
    path('videos/', views.video_list, name='video_list'),
    path('videos/<slug:slug>/', views.video_detail, name='video_detail'),

    # Missions
    path('missions/', views.mission_list, name='mission_list'),
    path('missions/<slug:slug>/', views.mission_detail, name='mission_detail'),

    # About & Contact
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    
    # Broadcast
    path('broadcast/', views.broadcast_list, name='broadcast_list'),
    path('broadcast/<slug:slug>/', views.broadcast_detail, name='broadcast_detail'),
    
    # Broadcast
    path('give/', views.give, name='give'),
]
