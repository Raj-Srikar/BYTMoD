from django.urls import path
from . import views

urlpatterns = [
	path('', views.get_link, name='home'),
	path('yt-link/', views.yt_link, name="YtForm"),
	path('video', views.video, name='video')
 ]