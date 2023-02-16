from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.core.cache import cache

from common.views import TitleMixin
from products.models import Cart, Product, ProductCategory


class IndexView(TitleMixin, TemplateView):
    template_name = 'products/index.html'
    title = 'Store'

    # def get_context_data(self, **kwargs):
    #     context = super(IndexView, self).get_context_data()
    #     context['title'] = 'Store'
    #     return context


# def index(request):
#     context = {
#         'title': 'Store',
#     }
#     return render(request, 'products/index.html', context)


class ProductsListView(TitleMixin, ListView):
    model = Product
    template_name = 'products/products.html'
    context_object_name = 'products'
    paginate_by = 2
    title = 'Store - Каталог'

    def get_queryset(self):
        query_set = super(ProductsListView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        return query_set.filter(category_id=category_id) if category_id else query_set

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsListView, self).get_context_data()
        categories = cache.get('categories')
        if not categories:
            context['categories'] = ProductCategory.objects.all()
            cache.set('categories', context['categories'], 30)
        else:
            context['categories'] = categories
        return context


# def products(request, category_id=0, page_num=1):
#     products = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
#     paginator = Paginator(products, per_page=3)
#     products_paginator = paginator.page(page_num)
#     context = {
#         'title': 'Store - Каталог',
#         'products': products_paginator,
#         'categories': ProductCategory.objects.all(),
#         'selected_cat': category_id,
#     }
#     return render(request, 'products/products.html', context)


@login_required
def cart_add(request, product_id):
    product = Product.objects.get(id=product_id)
    carts = Cart.objects.filter(user=request.user, quantity=1)

    if not carts.exists() or product not in carts:
        Cart.objects.create(user=request.user, product=product, quantity=1)
    else:
        cart = carts.first()
        cart.quantity += 1
        cart.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def cart_remove(request, cart_id):
    cart = Cart.objects.get(id=cart_id)
    cart.delete()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])
