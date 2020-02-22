from django.shortcuts import render, redirect 
from django.http import HttpResponse, JsonResponse
from .forms import *
from .models import Product
from django.contrib.auth.models import User
from .serializers import ProductSerializer
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

# Create your views here. 
def index(request): 
  
    if request.method == 'POST': 
        form = ProductForm(request.POST, request.FILES) 
  
        if form.is_valid(): 
            form.save() 
            return redirect('success') 
    else: 
        form = ProductForm() 
    return render(request, 'index.html', {'form' : form}) 


def display_products(request):
    if request.method == 'GET': 
  
        # getting all the objects of hotel. 
        Products = Product.objects.all()  
        return render(request, 'display_product_images.html', {'product_images' : Products}) 
  
  
def success(request): 
    return HttpResponse('successfully uploaded') 


@csrf_exempt
def product_list(request):

    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True, context={'request': request})
        print(serializer.data)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def product_detail(request, pk):

    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProductSerializer(product, context={'request': request})
        return JsonResponse(serializer.data)
