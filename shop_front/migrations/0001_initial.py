# Generated by Django 4.1.1 on 2022-09-23 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Item",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("item_name", models.CharField(max_length=100)),
                ("item_sub_name", models.CharField(max_length=100)),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("S", "Shirt"),
                            ("SP", "Sport Wear"),
                            ("OW", "Out Wear"),
                        ],
                        max_length=2,
                    ),
                ),
            ],
        ),
    ]
