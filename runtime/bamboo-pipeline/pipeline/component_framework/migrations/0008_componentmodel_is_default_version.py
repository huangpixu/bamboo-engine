# Generated by Django 3.2.15 on 2023-12-07 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("component_framework", "0007_auto_20201112_2244"),
    ]

    operations = [
        migrations.AddField(
            model_name="componentmodel",
            name="is_default_version",
            field=models.BooleanField(default=False, verbose_name="是否是默认版本"),
        ),
    ]
