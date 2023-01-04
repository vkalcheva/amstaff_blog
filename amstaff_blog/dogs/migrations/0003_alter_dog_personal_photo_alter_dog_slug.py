# Generated by Django 4.1.4 on 2022-12-21 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dogs", "0002_alter_dog_personal_photo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dog",
            name="personal_photo",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="dog",
            name="slug",
            field=models.SlugField(blank=True, unique=True),
        ),
    ]