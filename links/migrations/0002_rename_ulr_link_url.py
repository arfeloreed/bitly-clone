# Generated by Django 4.2.4 on 2023-08-30 04:31

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("links", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="link",
            old_name="ulr",
            new_name="url",
        ),
    ]