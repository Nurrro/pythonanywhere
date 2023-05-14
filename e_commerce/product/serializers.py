from rest_framework import serializers
from .models import Producte,Atribute,Category,Photo,Order,OrderItem

class ProducteSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Producte
        fields ="__all__" 
        # ('title','description','content','category')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields ="__all__" 
        # ('title','description')

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = "__all__"

class AtributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atribute
        fields = "__all__"
        # ('title','value','products')

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"       

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"       