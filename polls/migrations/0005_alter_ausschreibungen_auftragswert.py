# Generated by Django 3.2.6 on 2021-10-18 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_alter_ausschreibungen_datumnotifikation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ausschreibungen',
            name='Auftragswert',
            field=models.CharField(max_length=200),
        ),
    ]
