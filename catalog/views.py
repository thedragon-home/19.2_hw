from catalog.models import Product

from django.shortcuts import render, get_object_or_404


# Create your views here.

def home(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'home_temp.html', context)


def home_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'home_product.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}): {message}')

    return render(request, 'contacts.html')