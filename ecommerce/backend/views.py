from django.shortcuts import render

from .models.product import Products, Pictures


def index(request):
    products = Products.objects.all()
    pictures = Pictures.objects.all()
    context = {
        'products': products,
        'pictures': pictures,
    }

    return render(request, 'index.html', context)


def details(request, id):
    product = Products.objects.get(number=id)
    pictures = Pictures.objects.filter(product=product)
    mini_picture = Pictures.objects.filter(product=product).first()
    context = {
        'product': product,
        'pictures': pictures,
        'mini_picture': mini_picture,
    }

    return render(request, 'details.html', context)
