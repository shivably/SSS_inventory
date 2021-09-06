from django.http import HttpResponse
from .models import Product
from django.template import loader
from django.http import Http404
from django.shortcuts import render

def product(request):
    product_list = Product.objects.order_by('price_in_dollars')
    template = loader.get_template('product/list.html')
    context = {
        'product_list': product_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'product/details.html', {'product': product})

def add(request):

    if request.method == 'GET':
        template = loader.get_template('product/add.html')
        context = {}
        return HttpResponse(template.render(context, request))
    if request.method == 'POST':
        name = request.POST.get('name', None)
        dsc = request.POST.get('description', None)
        mft = request.POST.get('manufacturer', None)
        price = request.POST.get('price_in_dollars', None)

        new_product = Product(name=name, description=dsc, manufacturer=mft, price_in_dollars=price)
        new_product.save()

        product_list = Product.objects.order_by('price_in_dollars')
        template = loader.get_template('product/list.html')
        context = {
            'product_list': product_list,
        }
        return HttpResponse(template.render(context, request))