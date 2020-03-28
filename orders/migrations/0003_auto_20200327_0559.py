# Generated by Django 3.0.3 on 2020-03-27 05:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('payments', '0001_initial'),
        ('orders', '0002_delete_customerorderproduct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerorder',
            name='order_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='customerorder',
            name='order_status',
            field=models.CharField(
                choices=[('PND', 'Pending'), ('PAD', 'PAID'), ('AWD', 'AWAITING DELIVERY'), ('DLD', 'DELIVERED')],
                default='PND', max_length=3),
        ),
        migrations.AlterField(
            model_name='customerorder',
            name='payment_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='payment_for_order', to='payments.CustomerPayment'),
        ),
    ]