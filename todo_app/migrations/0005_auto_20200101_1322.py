# Generated by Django 3.0.1 on 2020-01-01 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0004_auto_20200101_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo_models',
            name='date_todo',
            field=models.DateField(blank=True, null=True),
        ),
    ]
