# Generated by Django 3.2 on 2021-04-10 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='book',
            table='bookinfo',
        ),
    ]
