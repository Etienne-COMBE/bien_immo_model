# Generated by Django 4.0 on 2022-01-07 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_view', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bien',
            name='etage',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='bien',
            name='prix_HT',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='bien',
            name='prix_m2_HT',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='bien',
            name='prix_m2_TTC',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='bien',
            name='prix_tva_normale',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='bien',
            name='prix_tva_reduite',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='bien',
            name='surface',
            field=models.FloatField(null=True),
        ),
    ]
