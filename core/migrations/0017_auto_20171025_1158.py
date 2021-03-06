# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 13:58
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        ('core', '0016_auto_20171022_1909'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=60)),
                ('state_province', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=50)),
                ('cpf', models.CharField(blank=True, max_length=11, null=True, unique=True, verbose_name='CPF')),
                ('rg', models.CharField(blank=True, max_length=11, null=True, verbose_name='RG')),
            ],
            options={
                'verbose_name': 'comprador',
                'verbose_name_plural': 'compradores',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Saler',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=60)),
                ('state_province', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=50)),
                ('cnpj', models.CharField(blank=True, max_length=14, null=True, unique=True, verbose_name='CNPJ')),
                ('ie', models.CharField(blank=True, max_length=12, null=True, verbose_name='inscrição estadual')),
            ],
            options={
                'verbose_name': 'vendedor',
                'verbose_name_plural': 'vendedores',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='customer',
            name='category',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='user_ptr',
        ),
        migrations.RemoveField(
            model_name='buyevent',
            name='category',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.AddField(
            model_name='buyevent',
            name='buyerid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Buyer'),
        ),
    ]
