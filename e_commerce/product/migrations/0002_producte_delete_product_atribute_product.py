# Generated by Django 4.2 on 2023-04-18 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('description', models.CharField(max_length=150)),
                ('content', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='product.category')),
                ('tags', models.ManyToManyField(to='product.atribute')),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.AddField(
            model_name='atribute',
            name='product',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, related_name='atribute', to='product.producte'),
        ),
    ]
