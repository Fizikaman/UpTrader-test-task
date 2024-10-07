from django.shortcuts import render
from django.urls import path
from .views import MenuViewSet

menu_detail = MenuViewSet.as_view({
    'get': 'retrieve',
})

urlpatterns = [
    path('api/menus/<str:pk>/', menu_detail, name='menu-detail'),
]
