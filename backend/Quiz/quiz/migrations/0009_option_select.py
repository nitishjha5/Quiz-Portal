# Generated by Django 3.1 on 2020-09-06 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0008_remove_quiz_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='option',
            name='select',
            field=models.BooleanField(default=False),
        ),
    ]
