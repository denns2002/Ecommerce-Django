from django.shortcuts import render

from .models.product import Products, Pictures, PokemonTypes, PokemonWeaknesses
from .models.types import Types


def search(request):
    if request.method == 'POST':
        pictures = Pictures.objects.all()
        searched = request.POST['searched']
        results = Products.objects.filter(
                name__contains=searched,
            ) | Products.objects.filter(
                number__contains=searched,
            )

        context = {
            'searched': searched,
            'results': results,
            'pictures': pictures,
        }

        return render(request, 'search.html', context)
    else:
        context = {
                
            }

        return render(request, 'search.html', context)
        


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
    types = Types.objects.all()
    context = {
        'product': product,
        'pictures': pictures,
        'mini_picture': mini_picture,
        'types': types,
    }

    return render(request, 'details.html', context)
