# Generated by Django 2.2.7 on 2019-12-19 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='date_created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='todoitem',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]