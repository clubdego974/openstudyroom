# Generated by Django 3.1.14 on 2022-10-12 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0011_auto_20221012_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='ogs_username',
            field=models.CharField(blank=True, max_length=60),
        ),
    ]