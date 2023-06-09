# Generated by Django 4.1.3 on 2023-04-19 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BESK', '0009_projectimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Kullanıcı Adı')),
                ('phone', models.CharField(max_length=255, verbose_name='Kullanıcı Telefonu')),
                ('email', models.CharField(max_length=255, verbose_name='Kullanıcı Email')),
                ('message', models.TextField(verbose_name='Kullanıcı Adı')),
            ],
        ),
    ]
