# Generated by Django 4.2.16 on 2025-04-10 21:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_provincia_id_comunas_provincia_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comunas',
            name='provincia',
        ),
        migrations.RemoveField(
            model_name='descuentos',
            name='tipo_descuento',
        ),
        migrations.RemoveField(
            model_name='empresa',
            name='precio',
        ),
        migrations.DeleteModel(
            name='nacionalidad',
        ),
        migrations.RemoveField(
            model_name='provincias',
            name='region',
        ),
        migrations.RemoveField(
            model_name='sedes',
            name='comuna',
        ),
        migrations.RemoveField(
            model_name='sedes',
            name='empresa',
        ),
        migrations.DeleteModel(
            name='tipo_empresa',
        ),
        migrations.DeleteModel(
            name='comunas',
        ),
        migrations.DeleteModel(
            name='descuentos',
        ),
        migrations.DeleteModel(
            name='empresa',
        ),
        migrations.DeleteModel(
            name='precios',
        ),
        migrations.DeleteModel(
            name='provincias',
        ),
        migrations.DeleteModel(
            name='regiones',
        ),
        migrations.DeleteModel(
            name='sedes',
        ),
        migrations.DeleteModel(
            name='tipo_descuentos',
        ),
    ]
