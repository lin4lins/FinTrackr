# Generated by Django 4.2.1 on 2023-06-11 10:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0003_account_color"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transaction",
            name="note",
            field=models.CharField(blank=True, max_length=255),
        ),
    ]