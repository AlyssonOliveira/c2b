# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-01 11:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BuyEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=19)),
                ('like', models.IntegerField(default=0)),
                ('model_pic', models.ImageField(default='img/no-img.jpg', upload_to='pic_folder/')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, null=True)),
                ('address', models.CharField(max_length=50, null=True)),
                ('city', models.CharField(max_length=60, null=True)),
                ('state_province', models.CharField(max_length=30, null=True)),
                ('country', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('typecustomer', models.BooleanField(default=True)),
                ('cnpjcpf', models.CharField(max_length=14, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='buyevent',
            name='category',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.Category'),
        ),
    ]
