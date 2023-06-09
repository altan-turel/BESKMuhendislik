# Generated by Django 4.1.3 on 2023-04-19 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BESK', '0002_birim_program'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=4, verbose_name='Proje Yılı')),
                ('name', models.CharField(max_length=155, verbose_name='Proje Adı')),
                ('who', models.CharField(max_length=50, verbose_name='Proje Kimin?')),
                ('start', models.DateField(verbose_name='Proje Başlama Tarihi')),
                ('finish', models.DateField(verbose_name='Proje Bitiş Tarihi')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Proje Tutarı')),
            ],
        ),
    ]
