# Generated by Django 2.1.7 on 2019-03-22 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('park', '0008_balance_positionbind'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='hygiene',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='comment',
            name='platform',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='comment',
            name='service',
            field=models.IntegerField(default=0),
        ),
    ]
