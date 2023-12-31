# Generated by Django 4.2.7 on 2023-11-16 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_rename_is_sale_product_on_sale'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
        ),
    ]
