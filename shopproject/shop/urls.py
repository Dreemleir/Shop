from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.index, name='index'),
    path('success/', views.success, name = 'success'),
    path('all/', views.display_products, name='product_images')
]

