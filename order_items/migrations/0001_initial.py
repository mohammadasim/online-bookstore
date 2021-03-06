# Generated by Django 3.0.3 on 2020-04-01 05:23

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('quantity', models.IntegerField(default=1)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='books.Book')),
            ],
        ),
    ]
