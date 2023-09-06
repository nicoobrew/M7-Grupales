from django.contrib import admin
from django.urls import path
from . views import Index, Details, welcome_page, create_order, confirmed_order, orders, OrderDetails, modification, create_orderCliente, pedidos_Cliente

app_name = "store"

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('welcome', welcome_page, name='welcome'),
    path('details/<int:pk>', Details.as_view(), name='details'),
    path('new_order', create_order, name='new_order'),
    path('confirmed_order/<int:order_id>/', confirmed_order, name='confirmed_order'),
    path('orders', orders, name='orders'),
    path('order_detail/<int:pk>', OrderDetails.as_view(), name='order_details'),
    path('modification_order/<int:order_id>', modification, name='modification_order'),
    path('hacer_pedido/', create_orderCliente, name='hacer_pedido'),
    path('tus_pedidos/', pedidos_Cliente, name='tus_pedidos'),
]
