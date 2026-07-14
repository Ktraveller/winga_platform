from django.shortcuts import get_object_or_404, render
from core.models import Product

def products(request):
    products1 = Product.objects.order_by('?')[:50]
    products2 = Product.objects.order_by('?')[:50]
    products3 = Product.objects.order_by('?')[:50]
    products4 = Product.objects.order_by('?')[:50]
    products5 = Product.objects.order_by('?')[:100]
    products_l = Product.objects.order_by('?')[:10]
    like_products = Product.objects.order_by('?')[:15]
    return render(request, 'products.html', {
        'products1': products1,
        'products2': products2,
        'products3': products3,
        'products4': products4,
        'products5': products5,
        'products_l': products_l,
        'like_products': like_products
    })



def preview_products(request, id):
    product = get_object_or_404(Product, id=id)
    products1 = Product.objects.order_by('?')[:50]
    products2 = Product.objects.order_by('?')[:50]
    products3 = Product.objects.order_by('?')[:50]
    products4 = Product.objects.order_by('?')[:50]
    products5 = Product.objects.order_by('?')[:100]
    products_l = Product.objects.order_by('?')[:10]
    return render(request, 'product_details.html', {
        'product': product,
        'products1': products1,
        'products2': products2,
        'products3': products3,
        'products4': products4,
        'products5': products5,
        'products_l': products_l
    })


def filter_products(request, category):
    if category == 'sort':
        products1 = Product.objects.order_by('?')[:50]
        products2 = Product.objects.order_by('?')[:50]
        products3 = Product.objects.order_by('?')[:50]
        products4 = Product.objects.order_by('?')[:50]
        products5 = Product.objects.order_by('?')[:100]
        products_l = Product.objects.order_by('?')[:10]
        like_products = Product.objects.order_by('?')[:15]
        return render(request, 'products.html', {
            'products1': products1,
            'products2': products2,
            'products3': products3,
            'products4': products4,
            'products5': products5,
            'products_l': products_l,
            'like_products': like_products
        })
    
    elif category == 'filter':
        products1 = Product.objects.order_by('?')[:50]
        products2 = Product.objects.order_by('?')[:50]
        products3 = Product.objects.order_by('?')[:50]
        products4 = Product.objects.order_by('?')[:50]
        products5 = Product.objects.order_by('?')[:100]
        products_l = Product.objects.order_by('?')[:10]
        like_products = Product.objects.order_by('?')[:15]
        return render(request, 'products.html', {
            'products1': products1,
            'products2': products2,
            'products3': products3,
            'products4': products4,
            'products5': products5,
            'products_l': products_l,
            'like_products': like_products
        })
    
    else:
        products1 = Product.objects.order_by('?').filter(category=category)[:50]
        products2 = Product.objects.order_by('?').filter(category=category)[:50]
        products3 = Product.objects.order_by('?').filter(category=category)[:50]
        products4 = Product.objects.order_by('?').filter(category=category)[:50]
        products5 = Product.objects.order_by('?').filter(category=category)[:100]
        products_l = Product.objects.order_by('?').filter(category=category)[:10]
        like_products = Product.objects.order_by('?').filter(category=category)[:15]
        return render(request, 'products.html', {
            'products1': products1,
            'products2': products2,
            'products3': products3,
            'products4': products4,
            'products5': products5,
            'products_l': products_l,
            'like_products': like_products
        })
