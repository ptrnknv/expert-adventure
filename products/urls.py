from django.urls import path

from products.views import products, cart_add, cart_remove

app_name = 'products'

urlpatterns = [
    path('', products, name='index'),
    path('category/<int:category_id>/page/<int:page_num>/', products, name='catinator'),
    path('page/<int:page_num>/', products, name='paginator'),
    path('carts/add/<int:product_id>/', cart_add, name='cart_add'),
    path('carts/remove/<int:cart_id>/', cart_remove, name='cart_remove'),
]
