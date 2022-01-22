# Generated by Django 2.2.24 on 2022-01-21 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0009_auto_20210504_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leagueevent',
            name='event_type',
            field=models.CharField(choices=[('ladder', 'ladder'), ('league', 'league'), ('meijin', 'meijin'), ('dan', 'dan'), ('ddk', 'ddk'), ('sdk', 'sdk'), ('tournament', 'tournament')], default='ladder', max_length=10),
        ),
    ]