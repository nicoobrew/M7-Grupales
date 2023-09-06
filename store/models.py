from django.db import models
from django.contrib.auth.models import AbstractUser, User
from users.models import CustomUser

# Create your models here.
class Product(models.Model):
    titulo = models.CharField(max_length=70)
    descripcion = models.TextField()
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to='store/img', default='store/img/default_image.jpg', null=True)

    def __str__(self):
        return self.titulo

class Order(models.Model):
    pay_choices = (
        ("Efectivo", "Efectivo"),
        ("Debito", "Debito"),
        ("Credito", 'Credito'),
    )

    order_status = (
        ("Pedido Pendiente", "Pedido Pendiente"),
        ("Pedido confirmado", "Pedido confirmado"),
        ("Pago aprobado", "Pago aprobado"),
        ("Pedido preparado","Pedido preparado"),
        ("Pedido Enviado/listo para recoger", "Pedido Enviado/listo para recoger"),
        ("Pedido Entregado", "Pedido Entregado"),
    )

    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=50, default='hola.adadis@outlook.com')
    direccion = models.CharField(max_length=100, default='En Sucursal')
    producto = models.ForeignKey(Product, on_delete=models.CASCADE)
    cantidad = models.IntegerField(null=True)
    precio = models.IntegerField(null=True)
    total = models.IntegerField(null=True)
    metodo_pago = models.CharField(choices=pay_choices, default='Efectivo')
    estado_pedido = models.CharField(choices=order_status, default='Pedido Pendiente')
    
class OrderCliente(models.Model):
    pay_choices = (
        ("Efectivo", "Efectivo"),
        ("Debito", "Debito"),
        ("Credito", 'Credito'),
    )

    nombre = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=50, default='hola.adadis@outlook.com')
    direccion = models.CharField(max_length=100, default='En Sucursal')
    producto = models.ForeignKey(Product, on_delete=models.CASCADE)
    cantidad = models.IntegerField(null=True)
    metodo_pago = models.CharField(choices=pay_choices, default='Efectivo')