# Generated by Django 2.2.7 on 2019-11-18 00:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_coment_descri'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coment',
            options={'permissions': (('Usuario', 'Es profesor'), ('adm', 'Es adm'))},
        ),
    ]
