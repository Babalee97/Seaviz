# Generated by Django 3.2.16 on 2022-11-24 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_dataload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataload',
            name='data',
            field=models.FileField(upload_to=''),
        ),
    ]
