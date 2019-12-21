# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-12-15 19:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('poste', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Bac',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacite', models.IntegerField()),
                ('etat_remplissage', models.CharField(max_length=255)),
                ('frequence_remplissage', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Coordonnees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.IntegerField(null=True)),
                ('longitude', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Registre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heure', models.DateTimeField(auto_now_add=True, verbose_name='date de modification')),
                ('bac', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Bac')),
            ],
        ),
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('poste', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='registre',
            name='utilisateur',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Utilisateur'),
        ),
        migrations.AddField(
            model_name='bac',
            name='coordonnees',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Coordonnees'),
        ),
    ]