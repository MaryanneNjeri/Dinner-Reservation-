# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-03 11:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Reserve', '0005_menu_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.IntegerField(max_length=40)),
                ('Payment_method', models.CharField(blank=True, choices=[('Cash', 'Cash'), ('M-pesa', 'M-pesa'), ('Credit_card', 'Credit_card'), ('Debit_card', 'Debit_card')], max_length=30, verbose_name='Payment_method')),
                ('Number_of_seats', models.CharField(max_length=40, null=True)),
                ('restaurant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Reserve.Restaurant')),
            ],
        ),
    ]