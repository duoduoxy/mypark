# Generated by Django 2.1.7 on 2019-03-23 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('park', '0010_auto_20190323_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='parkinfo',
            name='userID',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='user',
            name='payState',
            field=models.IntegerField(default=0),
        ),
    ]
