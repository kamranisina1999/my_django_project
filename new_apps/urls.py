from django.urls import path

from new_apps.views import index, main_page

urlpatterns =[
    path('index/', index),
    path('', main_page),
]
