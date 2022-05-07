"""digital_society URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('logout/', views.logout, name='logout'),
    path('add-member/', views.add_member, name='add-member'),
    path('my-profile/', views.my_profile, name='my-profile'),
    path('update-profile/', views.update_profile, name='update-profile'),
    path('all-member/', views.all_member, name='all-member'),
    path('maintenance/', views.maintenance, name='maintenance'),
    path('all-event/', views.all_event, name='all-event'),
    path('view-event/', views.view_event, name='view-event'),
    path('add-complain/', views.add_complain, name='add-complain'),
    path('list-complain/', views.list_complain, name='list-complain'),
    path('add-notice/', views.add_notice, name='add-notice'),  
    path('notice-board/', views.notice_board, name='notice-board'),  
    path('add-visitors/', views.add_visitors, name='add-visitors'),  
    path('all-visitors/', views.all_visitors, name='all-visitors'),
    path('add-photos/', views.add_photos, name='add-photos'), 
    path('photo-gallery/', views.photo_gallery, name='photo-gallery'), 
    path('add-video/', views.video_gallery, name='video-gallery'), 
    path('video-gallery/', views.add_video, name='add-video'), 
    path('add-suggestion/', views.add_suggestion, name='add-suggestion'), 
    path('view-suggestion/', views.view_suggestion, name='view-suggestion'), 
    path('forgot-password/', views.forgot_password, name='forgot-password'), 
    path('otp-verify/', views.otp_verify, name='otp-verify'), 
]
