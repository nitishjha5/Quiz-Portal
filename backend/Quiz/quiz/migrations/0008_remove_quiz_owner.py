# Generated by Django 3.1 on 2020-08-10 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0007_auto_20200809_1327'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='owner',
        ),
    ]
