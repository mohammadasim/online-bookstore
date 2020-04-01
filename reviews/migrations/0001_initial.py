# Generated by Django 3.0.3 on 2020-04-01 05:23

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=60)),
                ('type', models.CharField(choices=[('POS', 'Positive'), ('NEG', 'Negative'), ('NEU', 'Neutral')],
                                          max_length=20)),
                ('review', models.TextField(verbose_name='Review')),
                ('update_date', models.DateField(auto_now_add=True, verbose_name='Last Updated')),
            ],
        ),
    ]
