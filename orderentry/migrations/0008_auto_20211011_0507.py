# Generated by Django 3.2.7 on 2021-10-11 05:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orderentry', '0007_auto_20211011_0453'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderinfo',
            name='order_Item_Shipping',
        ),
        migrations.RemoveField(
            model_name='orderinfo',
            name='order_date',
        ),
        migrations.RemoveField(
            model_name='orderinfo',
            name='total_Cost',
        ),
        migrations.CreateModel(
            name='invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_Item_Shipping', models.CharField(choices=[('STANDARD', 'standard'), ('EXPEDITED', 'expedited'), ('2-DAY', '2-day')], default='STANDARD', max_length=20)),
                ('order_date', models.DateTimeField(verbose_name='order date')),
                ('total_Cost', models.IntegerField(default=0)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orderentry.customerinfo')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orderentry.orderinfo')),
            ],
            options={
                'verbose_name': 'Invoice',
                'verbose_name_plural': 'Invoices',
            },
        ),
    ]
