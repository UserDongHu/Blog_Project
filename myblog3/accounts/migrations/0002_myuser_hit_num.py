# Generated by Django 4.2.6 on 2023-11-05 03:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="myuser",
            name="hit_num",
            field=models.IntegerField(default=0),
        ),
    ]
