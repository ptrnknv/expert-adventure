from products.models import Cart


def carts(request):
    user = request.user
    return {'carts': Cart.objects.filter(user=user) if user.is_authenticated else []}
