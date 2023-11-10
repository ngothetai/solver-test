from django.urls import path
from . import views
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home , name="home"),
    # path('upload/', views.upload_file, name='upload_file'),
    path('upload/', views.process_form, name='upload_file'),
]