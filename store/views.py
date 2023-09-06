from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.contrib.auth.forms import AuthenticationForm
from .models import Product, Order
from .forms import OrderForm, PedidoClienteForm
from django.contrib import messages
from .models import Order, OrderCliente
import json
from django.contrib.auth.decorators import permission_required, user_passes_test
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required



# Create your views here.
class Index(generic.ListView):
    model = Product
    template_name = 'store/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_login"] = AuthenticationForm
        return context

class Details(generic.DetailView):
    model = Product
    template_name = 'store/product_details.html'

def welcome_page(request):
    return render(request, 'store/welcome.html')

'''
def importar():
    with open('data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        for item in data:
            fields = item['fields']
            nuevo_producto = Product(
                titulo=fields['titulo'],
                descripcion=fields['descripcion'],
                precio=fields['precio'],
                imagen=fields['imagen'],
            )
            nuevo_producto.save()

'''

# Vendedor
def is_vendedor(user):
    return user.groups.filter(name='vendedor').exists()

@user_passes_test(is_vendedor)
def create_order(request):
    if request.method == 'POST':
        form_order = OrderForm(request.POST)
        if form_order.is_valid():
            order = form_order.save(commit=False)
            order.precio = order.producto.precio
            order.total = order.precio * order.cantidad
            order.save()
            order_id = order.pk 
            return redirect("store:confirmed_order", order_id)
        else:
            messages.error(request, "Hubo un error en el registro del pedido, verifica bien antes de continuar")
    form_order = OrderForm()
    return render(request, "store/new_order.html", {'form_order': form_order})

@user_passes_test(is_vendedor)
def confirmed_order(request, order_id):
    order = Order.objects.get(pk=order_id)
    return render(request, "store/confirmed_order.html", {'order': order})

def is_logistica_o_vendedor(user):
    # return user.has_perm('logistica') or user.has_perm('vendedor')
    return is_logistica(user) or is_vendedor(user)

# Logistica

def is_logistica(user):
    return user.groups.filter(name='logistica').exists()

@user_passes_test(is_logistica_o_vendedor)
def orders(request):
    orders = Order.objects.all()
    return render(request, "store/orders.html", {'orders': orders})

@method_decorator(user_passes_test(is_logistica), name='dispatch')
class OrderDetails(generic.DetailView):
    model = Order
    template_name = 'store/order_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order = get_object_or_404(Order, pk=self.kwargs['pk'])
        context['form'] = OrderForm(instance=order)
        return context

    def post(self, request, *args, **kwargs):
        target = Order.objects.get(pk=self.kwargs['pk'])
        form_order = OrderForm(request.POST, instance=target)
        if form_order.is_valid():
            order = form_order.save(commit=False)
            order.precio = order.producto.precio
            order.total = order.precio * order.cantidad
            order.save()
            return redirect("store:modification_order", order_id=self.kwargs['pk'])
        else:
            messages.error(request, "Hubo un error en el registro del pedido, verifica bien antes de continuar")

        return redirect('store:order_details', pk=self.kwargs['pk'])

def modification(request, order_id):
    order = Order.objects.get(pk=order_id)
    return render(request, "store/modification_order.html", {'order': order})

@login_required
def create_orderCliente(request):
    if request.method == 'POST':
        form_order = PedidoClienteForm(request.POST)
        if form_order.is_valid():
            order = form_order.save(commit=False)
            order.precio = order.producto.precio
            order.total = order.precio * order.cantidad
            order.save()
            order_id = order.pk 
            return redirect("store:confirmed_order", order_id)
        else:
            messages.error(request, "Hubo un error en el registro del pedido, verifica bien antes de continuar")
    form_order = PedidoClienteForm()
    return render(request, "store/hacer_pedidos.html", {'form_order': form_order})

@login_required
def pedidos_Cliente(request):
    pedidos = OrderCliente.objects.all()
    return render(request, "store/pedidos_cliente.html", {'pedidos': pedidos} )

