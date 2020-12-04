from django.urls import path, include
from .views import ReadDataApi

urlpatterns = [

    path('', ReadDataApi.as_view(), name='home'),
    path('api/read/', ReadDataApi.as_view(), name='read'),
]