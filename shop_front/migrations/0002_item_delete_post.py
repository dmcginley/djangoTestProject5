# Generated by Django 4.1.1 on 2022-09-22 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop_front", "0001_initial"),
    ]

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
                ("price", models.FloatField()),
                ("description", models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name="Post",
        ),
    ]