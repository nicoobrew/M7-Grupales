from django import forms
from .models import Order, OrderCliente

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['usuario', 'nombre', 'email', 'direccion' ,'producto', 'cantidad', 'metodo_pago', 'estado_pedido']

# class ModifyOrderForm(forms.ModelForm):
#     class Meta:
#         model = Order
#         fields = ['estado']

class PedidoClienteForm(forms.ModelForm):
    class Meta:
        model = OrderCliente
        fields = ['nombre', 'email', 'direccion' ,'producto', 'cantidad', 'metodo_pago']