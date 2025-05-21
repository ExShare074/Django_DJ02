# ZeroCoder/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    # теперь подключаем data_app без префикса
    path('', include('data_app.urls')),

    # main остаётся с теми же маршрутами
    path('', include('main.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)