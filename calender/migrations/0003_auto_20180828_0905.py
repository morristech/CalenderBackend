# Generated by Django 2.1 on 2018-08-28 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calender', '0002_auto_20180827_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='id',
            field=models.BigIntegerField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
