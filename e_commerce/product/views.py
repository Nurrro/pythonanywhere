from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated, AllowAny
from urllib import response
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from django.shortcuts import render,HttpResponse
from .models import*
from product.serializers import*
from rest_framework.viewsets import ModelViewSet
from product.pagination import ProductAPIListPagination

#home functions
def index(request):
    product= Producte.objects.all()
    categoory = Category.objects.all()
    atribute = Atribute.objects.all()
    
    context={
        'product':product,
        'categoory': categoory,
        'atribute':atribute,
    }
    return render(request,'index.html',context)

def all_products(request):
    product= Producte.objects.all()
    categoory = Category.objects.all()
    atribute = Atribute.objects.all()
    
    context={
        'product':product,
        'categoory': categoory,
        'atribute':atribute,
    }
    return render(request,'all_prod.html',context)


#value product
def detail_product(request, id):
    product = Producte.objects.get(id=id)
    atribute = Atribute.objects.all()
    category = Category.objects.all()

    context = {
        'product' : product,
        'atribute' : atribute,
        'category' : category
    }
    return render (request , 'prod_atrib.html', context)

#detail category
def detail_category(request, id):
    product = Producte.objects.all()
    atribute = Atribute.objects.all()
    category = Category.objects.get(id=id)

    context = {
        'product' : product,
        'atribute' : atribute,
        'category' : category
    }
    return render (request , 'category_product.html', context)

def zakaz(request):
    product = Producte.objects.all()
    order = Order.objects.all()
    orderitem = OrderItem.objects.all()
    context = {
        'product' : product,
        'order' : order,
        'orderitem' : orderitem,
    }
    return render(request, 'zakazy.html',context)    


#API Products
class ProducteModelViewSet(ModelViewSet):
    queryset = Producte.objects.all()
    serializer_class = ProducteSerializer
    permission_classes = (IsAuthenticated, ) 
    pagination_class = ProductAPIListPagination
    # authentication_classes = (TokenAuthentication ,) 

#API Category
class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated, )  


#API Atribute
class AtributeModelViewSet(ModelViewSet):
    queryset = Atribute.objects.all()
    serializer_class = AtributeSerializer
    permission_classes = (IsAuthenticated, ) 

#API Photo
class PhotoModelViewSet(ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = (IsAuthenticated, )

class OrderItemModelViewSet(ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = (IsAuthenticated, )

class OrderModelViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated, )

# Create your views here.


