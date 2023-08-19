from django.db import models
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from chain.forms import ProductForm
from chain.models import Model, Price, Manufacture, Product


def index(request):
    return render(request, "chain/index.html", {
        'form': ProductForm(),
        'objs': Product.objects.all(),
    })


def get_model_by_manufacture(request):
    form = ProductForm()
    try:
        manufacture_id = int(request.GET.get('manufacture'))
    except:
        manufacture_id = Manufacture.objects.create(name=request.GET.get('manufacture'))

    form.fields['model'].queryset = Model.objects.filter(manufacture_id=manufacture_id)

    return render(request, 'chain/form.html', {
        'form': form
    })


def get_price_by_model(request):
    form = ProductForm()
    try:
        manufacture_id = int(request.GET.get('manufacture'))
    except:
        manufacture, _ = Manufacture.objects.get_or_create(name=request.GET.get('manufacture'))
        manufacture_id = manufacture.id

    try:
        model_id = int(request.GET.get('model'))
        manufacture_id = int(request.GET.get('manufacture'))
    except:
        model, _ = Model.objects.get_or_create(name=request.GET.get('model'), manufacture_id=manufacture_id)
        model_id = model.id
    form.fields['price'].queryset = Price.objects.filter(model_id=model_id)

    return render(request, 'chain/form.html', {
        'form': form
    })


def add(request):
    if request.method == "POST":
        product = Product.objects.create(price_id=request.POST.get('price'))
        return render(request, 'chain/product.html', {'product': product})
    return HttpResponse('', status=404)


def add_price(request):
    form = ProductForm()
    try:
        model_id = int(request.GET.get('model'))
    except:
        model = Model.objects.get(name=request.GET.get('model'))
        model_id = model.id
    Price.objects.get_or_create(price=request.GET.get('price'), model_id=model_id)

    form.fields['price'].queryset = Price.objects.filter(model_id=model_id)
    return render(request, 'chain/form.html', {
        'form': form
    })


def search(request):
    q = request.GET.get('q', '')
    manufactures = Manufacture.objects.filter(name__icontains=q).annotate(value=models.F('id'), text=models.F('name')).values('value', 'text') if q else Manufacture.objects.all()[:5]

    return JsonResponse({'items': list(manufactures)}, safe=False)