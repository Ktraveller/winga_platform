from django.http import HttpResponse
from django.shortcuts import render
from core.models import Product


def home(request):
    products = Product.objects.order_by('?')[:50]
    return render(request, 'index.html', {
        'products': products,
    })



# Favorite
def favorities(request):
    favorite_products = Product.objects.order_by('?')[:50]
    return render(request, 'favorities.html', {
        'favorite_products': favorite_products,
    })


# search
def search(request):
    search_result = Product.objects.order_by('?')
    return render(request, 'search.html', {
        'search_result': search_result,
    })


# Category
def categories(request):
    return render(request, 'categories.html', {})


# about use page
def about(request):
    return render(request, 'about.html', {})


# web check that print "OK"
def health_check(request):
    return HttpResponse("OK", content_type="text/plain")
