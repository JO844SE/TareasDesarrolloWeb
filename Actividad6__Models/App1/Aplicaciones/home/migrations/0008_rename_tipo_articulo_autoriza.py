# Generated by Django 3.2.6 on 2021-09-05 02:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20210904_2045'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articulo',
            old_name='tipo',
            new_name='Autoriza',
        ),
    ]