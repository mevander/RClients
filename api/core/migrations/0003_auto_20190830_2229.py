# Generated by Django 2.2.4 on 2019-08-31 01:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190830_1242'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='cliente',
            table='Cliente',
        ),
        migrations.AlterModelTable(
            name='endereco',
            table='Endereco',
        ),
    ]