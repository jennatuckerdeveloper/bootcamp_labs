# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-03 17:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.IntegerField(default=100)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Food', max_length=100)),
                ('description', models.CharField(default="A day's food for your group.", max_length=300)),
                ('type', models.CharField(default='food', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
                ('type', models.CharField(default='item', max_length=100)),
                ('inventory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='game.Inventory')),
            ],
        ),
        migrations.CreateModel(
            name='Landmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='landmark',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='landmark', to='game.Landmark'),
        ),
        migrations.AddField(
            model_name='character',
            name='inventory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='characters', to='game.Inventory'),
        ),
    ]
