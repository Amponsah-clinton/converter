from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('convert/', views.convert_image, name='convert_image'),
    path('reduce/', views.reduce_image_size, name='reduce_image_size'),
    path('resize/', views.resize_image, name='resize_image'),
]
