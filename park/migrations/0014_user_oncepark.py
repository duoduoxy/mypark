# Generated by Django 2.1.7 on 2019-03-23 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('park', '0013_parkinfo_isbind'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='oncePark',
            field=models.IntegerField(default=0),
        ),
    ]