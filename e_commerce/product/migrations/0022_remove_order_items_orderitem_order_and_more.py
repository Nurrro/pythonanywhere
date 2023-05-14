# Generated by Django 4.2 on 2023-05-11 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0021_alter_order_user_alter_orderitem_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='items',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='items', to='product.order'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='product.producte'),
        ),
    ]
