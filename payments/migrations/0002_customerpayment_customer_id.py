# Generated by Django 3.0.3 on 2020-04-01 05:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerpayment',
            name='customer_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT,
                                    related_name='payments', to=settings.AUTH_USER_MODEL),
        ),
    ]