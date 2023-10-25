from django.urls import path, include
from . import views


urlpatterns = [
    path('products/', views.get_product_list, name='product-list'),
    path('order/create', views.create_order, name='create-order'),
    path('payment/create', views.create_payment, name='create-payment'),
]
