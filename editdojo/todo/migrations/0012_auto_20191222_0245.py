# Generated by Django 2.2.7 on 2019-12-21 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0011_auto_20191222_0233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='date_created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
