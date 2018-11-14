# Generated by Django 2.1.2 on 2018-11-07 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('porownanie_cen', '0003_produkt_klucz'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produkt',
            name='klucz',
            field=models.CharField(db_column='klucz', max_length=128, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='produkt',
            name='kodtowaru',
            field=models.CharField(db_column='kodTowaru', max_length=128),
        ),
        migrations.AlterUniqueTogether(
            name='produkt',
            unique_together={('klucz', 'kontrahentkod', 'kontrahentcennik')},
        ),
    ]
