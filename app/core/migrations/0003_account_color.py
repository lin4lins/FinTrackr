# Generated by Django 4.2.1 on 2023-06-10 17:47

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0002_alter_category_type_alter_category_unique_together"),
    ]

    operations = [
        migrations.AddField(
            model_name="account",
            name="color",
            field=colorfield.fields.ColorField(
                default="#FF0000", image_field=None, max_length=18, samples=None
            ),
        ),
    ]
