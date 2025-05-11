# ZeroCoder/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # всё, что на /data/... → data_app
    path('data/', include('data_app.urls')),

    # всё, что на /new_post/, /new и / – → main
    path('', include('main.urls')),
]