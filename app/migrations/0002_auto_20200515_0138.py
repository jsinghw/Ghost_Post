# Generated by Django 3.0.6 on 2020-05-15 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='boast',
        ),
        migrations.AddField(
            model_name='post',
            name='is_boast',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
