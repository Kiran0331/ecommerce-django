from django.urls import path
from . import views

urlpatterns=[
    path('', views.homepage, name='homepage'),
    path('cart/',views.cart_view, name='cart'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('increase_quantity/<int:product_id>/', views.increase_quantity, name='increase_quantity'),
    path('decrease_quantity/<int:product_id>/', views.decrease_quantity, name="decrease_quantity"),
    path('checkout/', views.checkout_view, name='checkout'),
]