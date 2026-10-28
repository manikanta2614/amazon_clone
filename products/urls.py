from django.urls import path
from . import views


urlpatterns = [

    path('products/', views.product_list, name='product_list'),
    path(
        'product/<int:id>/',
        views.product_detail,
        name='product_detail'
    ),
     path(
        '',
        views.home,
        name='home'
    ),
    path(
    'category/<str:category>/',
    views.category_products,
    name='category_products'
    ),
    path('add-to-cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path(
    'order/<int:id>/',
    views.place_order,
    name='place_order'
    ),
    path('remove-from-cart/<int:id>/', views.remove_from_cart, name='remove_from_cart'),


]