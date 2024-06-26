# Generated by Django 5.0.3 on 2024-06-10 01:52

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Accommodation",
            fields=[
                (
                    "id",
                    models.CharField(max_length=255, primary_key=True, serialize=False),
                ),
                ("accreditation_number", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=255)),
                ("cell_number", models.CharField(max_length=20)),
                ("street_address", models.CharField(max_length=255)),
                ("nearest_campus", models.CharField(max_length=255)),
                ("residence_name", models.CharField(max_length=255)),
                ("university", models.CharField(max_length=50)),
            ],
            options={
                "db_table": "Accommodations",
            },
        ),
    ]
