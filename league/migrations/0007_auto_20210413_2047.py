# Generated by Django 2.2.20 on 2021-04-13 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0006_leagueevent_servers'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='egf_id',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='egf_rank',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='profile',
            name='ffg_licence_number',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='ffg_rank',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]