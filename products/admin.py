from django.contrib import admin

from products.models import Cart, Product, ProductCategory

admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('name', 'description', ('price', 'quantity'), 'stripe_product_price_id', 'image', 'category')
    search_fields = ('name',)
    ordering = ('-name',)


class CartAdmin(admin.TabularInline):
    model = Cart
    fields = ('product', 'quantity', 'created_timestamp')
    readonly_fields = ('created_timestamp',)
    extra = 0
