# Generated by Django 4.1.4 on 2022-12-17 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Dog",
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
                ("name", models.CharField(max_length=30)),
                ("personal_photo", models.URLField()),
                ("location", models.CharField(blank=True, max_length=30, null=True)),
                ("date_of_birth", models.DateField(blank=True, null=True)),
            ],
        ),
    ]
