# Generated by Django 3.1 on 2020-09-07 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0015_auto_20200907_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='mark',
            field=models.IntegerField(default=0),
        ),
    ]
