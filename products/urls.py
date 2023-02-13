from django.urls import path

from products.views import ProductsListView, cart_add, cart_remove

app_name = 'products'

urlpatterns = [
    path('', ProductsListView.as_view(), name='index'),
    path('category/<int:category_id>/', ProductsListView.as_view(), name='category'),
    path('page/', ProductsListView.as_view(), name='paginator'),
    path('carts/add/<int:product_id>/', cart_add, name='cart_add'),
    path('carts/remove/<int:cart_id>/', cart_remove, name='cart_remove'),
]
