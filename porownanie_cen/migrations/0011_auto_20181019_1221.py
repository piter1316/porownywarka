# Generated by Django 2.1.2 on 2018-10-19 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('porownanie_cen', '0010_auto_20181019_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='logo',
            field=models.FileField(upload_to=''),
        ),
    ]
