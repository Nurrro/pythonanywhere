# Generated by Django 4.2 on 2023-04-30 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_remove_atribute_author_producte_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atribute',
            name='products',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prod_atrib', to='product.producte'),
        ),
    ]