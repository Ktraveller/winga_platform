from django.shortcuts import get_object_or_404, render
from core.models import Product

def products(request):
    products = Product.objects.order_by('?')[:100]
    other_products = Product.objects.order_by('?')[:50]
    like_products = Product.objects.order_by('?')[:15]
    return render(request, 'products.html', {
        'products': products,
        'other_products': other_products,
        'like_products': like_products
    })



def preview_products(request, id):
    product = get_object_or_404(Product, id=id)
    products = Product.objects.order_by('?')[:100]
    return render(request, 'product_details.html', {
        'product': product,
        'products': products
    })


def filter_products(request, category):
    if category == 'sort':
        products = Product.objects.order_by('title')[:50]
        other_products = Product.objects.order_by('title')[:100]
        like_products = Product.objects.order_by('title')[:15]

        return render(request, 'products.html', {
            'products': products,
            'other_products': other_products,
            'like_products': like_products,
        })
    elif category == 'filter':
        products = Product.objects.order_by('category')[:50]
        other_products = Product.objects.order_by('category')[:100]
        like_products = Product.objects.order_by('category')[:15]

        return render(request, 'products.html', {
            'products': products,
            'other_products': other_products,
            'like_products': like_products,
        })
    else:
        products = Product.objects.order_by('?').filter(category=category)[:50]
        other_products = Product.objects.order_by('?')[:100]
        like_products = Product.objects.order_by('?')[:15]
        return render(request, 'products.html', {
            'products': products,
            'other_products': other_products,
            'like_products': like_products,
        })
