# Generated by Django 2.1.7 on 2019-03-23 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('park', '0011_auto_20190323_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='parkinfo',
            name='carID',
            field=models.CharField(default='', max_length=20),
        ),
    ]