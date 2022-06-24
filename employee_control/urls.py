from django.contrib import admin
from django.urls import include, path
from app import urls as app_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(app_urls))
]
