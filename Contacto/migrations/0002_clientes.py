# Generated by Django 3.2 on 2021-04-27 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contacto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=250)),
                ('Telefono', models.CharField(max_length=15)),
                ('Renta', models.CharField(max_length=20)),
                ('Prevision', models.CharField(max_length=250)),
                ('Region', models.CharField(max_length=250)),
                ('Cargas', models.CharField(max_length=20)),
            ],
        ),
    ]