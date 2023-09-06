# Generated by Django 4.2.4 on 2023-08-22 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='direccion',
            field=models.TextField(default='Sin direccion', max_length=100),
        ),
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.EmailField(default='hola.adadis@outlook.com', max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='estado_pedido',
            field=models.CharField(choices=[('Pedido Pendiente', 'Pedido Pendiente'), ('Pedido confirmado', 'Pedido confirmado'), ('Pago aprobado', 'Pago aprobado'), ('Pedido preparado', 'Pedido preparado'), ('Pedido Enviado/listo para recoger', 'Pedido Enviado/listo para recoger'), ('Pedido Entregado', 'Pedido Entregado')], default='Pedido Pendiente'),
        ),
        migrations.AddField(
            model_name='order',
            name='metodo_pago',
            field=models.CharField(choices=[('Efectivo', 'Efectivo'), ('Debito', 'Debito'), ('Credito', 'Credito')], default='Efectivo'),
        ),
        migrations.AddField(
            model_name='order',
            name='nombre',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.DecimalField(decimal_places=2, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='cantidad',
            field=models.IntegerField(null=True),
        ),
    ]