# Generated by Django 2.1.7 on 2019-03-20 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('park', '0002_auto_20190320_1719'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('answerID', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.CharField(max_length=200)),
                ('commentID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='park.Comment')),
            ],
        ),
    ]
