from django.http import HttpResponse
from django.shortcuts import render
from core.models import Product


def home(request):
    products = Product.objects.order_by('?')[:20]
    fav_products = Product.objects.order_by('?')[:20]

    return render(request, 'index.html', {
        'products': products,
        'favorite_products': fav_products
    })


# about use page
def about(request):
    return render(request, 'about.html', {})


# web check that print "OK"
def health_check(request):
    return HttpResponse("OK", content_type="text/plain")