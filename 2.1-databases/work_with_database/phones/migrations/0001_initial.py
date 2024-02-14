# Generated by Django 5.0.1 on 2024-02-14 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Phone",
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
                ("name", models.CharField(max_length=50)),
                ("price", models.CharField(max_length=20)),
                ("image", models.CharField(default="0")),
                ("release_date", models.CharField(max_length=10)),
                ("lte_exists", models.BooleanField(default="False")),
                ("slug", models.SlugField(max_length=200)),
            ],
        ),
    ]
