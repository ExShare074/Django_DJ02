from django.urls import path
from . import views

urlpatterns = [
        path('new_post/', views.new_post, name='new_post'),
        path('new/', views.new),
        path('', views.index, name='index')
]
