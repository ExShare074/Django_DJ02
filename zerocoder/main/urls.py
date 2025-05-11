from django.urls import path
from . import views

urlpatterns = [
        path('', views.index),
        path('new_post/', views.new_post, name='new_post'),
        path('new', views.new),
        path('', views.index_view, name='index')
]
