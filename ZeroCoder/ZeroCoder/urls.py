from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    # main подключаем первым без префикса
    path('', include('main.urls')),

    # data_app теперь с префиксом data/
    path('data/', include('data_app.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)