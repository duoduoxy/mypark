# Generated by Django 2.1.7 on 2019-03-21 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('park', '0005_auto_20190321_1047'),
    ]

    operations = [
        migrations.AddField(
            model_name='parkinfo',
            name='isBusy',
            field=models.CharField(default='no', max_length=3),
        ),
    ]