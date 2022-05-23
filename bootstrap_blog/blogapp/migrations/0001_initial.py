# Generated by Django 4.0.3 on 2022-05-20 01:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('apellidoM', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=100)),
                ('pais', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='NombreFantasia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_fantasia', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TipoMensaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_mensaje', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Subcategoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('estado', models.BooleanField(default=True)),
                ('servicio', models.ManyToManyField(to='blogapp.servicio')),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razon_social', models.CharField(max_length=50)),
                ('contacto', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=100)),
                ('nombre_fantasia', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blogapp.nombrefantasia')),
                ('servicio', models.ManyToManyField(to='blogapp.servicio')),
            ],
        ),
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='nombre')),
                ('correo', models.EmailField(max_length=100, verbose_name='correo')),
                ('mensaje', models.CharField(max_length=200, verbose_name='mensaje')),
                ('tipo_mensaje', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blogapp.tipomensaje')),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('estado', models.BooleanField(default=True)),
                ('servicio', models.ManyToManyField(to='blogapp.servicio')),
                ('subcategoria', models.ManyToManyField(to='blogapp.subcategoria')),
            ],
        ),
    ]
