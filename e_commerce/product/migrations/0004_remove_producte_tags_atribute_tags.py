# Generated by Django 4.2 on 2023-04-24 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_atribute_options_alter_category_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producte',
            name='tags',
        ),
        migrations.AddField(
            model_name='atribute',
            name='tags',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='atribute', to='product.producte'),
        ),
    ]
