# Generated by Django 3.2.7 on 2021-10-05 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderentry', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderinfo',
            name='order_Item_Flavor',
            field=models.CharField(choices=[('CHOCOLATE', 'chocolate'), ('VANILLA', 'vanilla'), ('COOKIESNCREME', 'cookiesncreme'), ('STRAWBERRY', 'strawberry')], max_length=100),
        ),
    ]