# Generated by Django 3.0.3 on 2020-03-24 06:23

import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('payments', '0001_initial'),
        ('books', '0004_auto_20200324_0623'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerOrderProduct',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Book')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerOrder',
            fields=[
                ('order_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('order_status', models.CharField(
                    choices=[('PND', 'Pending'), ('CNF', 'CONFIRMED'), ('AWD', 'AWAITING DELIVERY'),
                             ('DLD', 'DELIVERED')], max_length=5)),
                ('order_date', models.DateField(auto_now_add=True, verbose_name='Order Date')),
                ('order_price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('customer_id', models.ForeignKey(default='anonymous', on_delete=django.db.models.deletion.SET_DEFAULT,
                                                  related_name='orders', to=settings.AUTH_USER_MODEL)),
                ('payment_id',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment_for_order',
                                   to='payments.CustomerPayment')),
            ],
        ),
    ]