from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home , name="home"),
    path('convex_hull/', views.convex_hull, name='convex_hull'),
    path('upload/', views.upload_file, name='upload_file'),
]