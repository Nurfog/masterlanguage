# Generated by Django 4.2.16 on 2025-04-14 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_colegio_comuna_alter_comuna_provincia_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comuna',
            name='provincia',
        ),
        migrations.RemoveField(
            model_name='empresa',
            name='comuna',
        ),
        migrations.RemoveField(
            model_name='provincia',
            name='region',
        ),
        migrations.RemoveField(
            model_name='region',
            name='pais',
        ),
        migrations.RemoveField(
            model_name='representante',
            name='comunas',
        ),
        migrations.RemoveField(
            model_name='representante',
            name='empresa',
        ),
        migrations.DeleteModel(
            name='colegio',
        ),
        migrations.DeleteModel(
            name='comuna',
        ),
        migrations.DeleteModel(
            name='empresa',
        ),
        migrations.DeleteModel(
            name='pais',
        ),
        migrations.DeleteModel(
            name='provincia',
        ),
        migrations.DeleteModel(
            name='region',
        ),
        migrations.DeleteModel(
            name='representante',
        ),
    ]
