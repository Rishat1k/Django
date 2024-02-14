from django.shortcuts import render, redirect
from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')
    if sort is not None:
        if sort == 'min_price':
            sort = 'price'
        elif sort == 'max_price':
            sort = '-price'
        phones_objects = Phone.objects.all().order_by(sort)
    else:
        phones_objects = Phone.objects.all()
    context = {'phones': phones_objects}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug=slug)[0]
    context = {'phone': phone}
    return render(request, template, context)
