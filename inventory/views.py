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