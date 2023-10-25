from django.urls import path, include
from . import views
from solver import views


urlpatterns = [
    path('/', views.home , name="home"),
    path('/solver/', )
]