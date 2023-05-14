from django.contrib import admin
from django.urls import path,include, re_path
from rest_framework.routers import DefaultRouter
from product.yasg import urlpatterns as doc_url

# from ecommerce import product
from . views import*

router = DefaultRouter()

router.register('products',ProducteModelViewSet)
router.register('atributes',AtributeModelViewSet)
router.register('category', CategoryModelViewSet)
router.register('photo', PhotoModelViewSet)
router.register('orderitem', OrderItemModelViewSet)
router.register('order', OrderModelViewSet)

urlpatterns = [
    path('',include(router.urls)),#список api адресов
    path('auth/', include('djoser.urls')),#добавление пользователей и список пользователей
    re_path(r'^auth/', include('djoser.urls.authtoken')),#new
]


#swagger urls
urlpatterns+=doc_url

#template tags
#path ('product/<int:id>/:atribute/', detail_product, name='product-values'),
# path('cat/product/<int:id>',detail_category, name='detail-cat' ),
# path('products/all/', all_products, name='all-products'),
#  path('home/',index,name='home'),
# path('zakazy/', zakaz, name='zakazy')
