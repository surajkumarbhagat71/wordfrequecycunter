# Generated by Django 2.2.7 on 2021-01-31 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wordstok',
            name='word',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
