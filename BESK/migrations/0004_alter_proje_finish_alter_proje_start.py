# Generated by Django 4.1.3 on 2023-04-19 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BESK', '0003_proje'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proje',
            name='finish',
            field=models.CharField(max_length=50, verbose_name='Proje Bitiş Tarihi'),
        ),
        migrations.AlterField(
            model_name='proje',
            name='start',
            field=models.CharField(max_length=50, verbose_name='Proje Başlama Tarihi'),
        ),
    ]