from django.contrib import admin
from django.urls import path

from new_apps.views import index, main_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index),
    path('', main_page),
]
