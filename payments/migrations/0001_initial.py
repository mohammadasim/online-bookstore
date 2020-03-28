# Generated by Django 3.0.3 on 2020-03-24 06:23

import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerPayment',
            fields=[
                ('payment_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('payment_date', models.DateField(auto_now_add=True, verbose_name='Payment Date')),
                ('customer_id', models.ForeignKey(default='anonymous', on_delete=django.db.models.deletion.SET_DEFAULT,
                                                  related_name='order', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]