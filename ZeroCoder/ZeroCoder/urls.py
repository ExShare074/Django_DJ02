# ZeroCoder/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # теперь подключаем data_app без префикса
    path('', include('data_app.urls')),

    # main остаётся с теми же маршрутами
    path('', include('main.urls')),
]