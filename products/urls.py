from django.urls import path

from products.views import products, cart_add, cart_remove

app_name = 'products'

urlpatterns = [
    path('', products, name='index'),
    path('carts/add/<int:product_id>/', cart_add, name='cart_add'),
    path('carts/remove/<int:cart_id>/', cart_remove, name='cart_remove'),
]
