# Generated by Django 4.2.7 on 2024-04-22 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lessons", "0005_module_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="module",
            name="slug",
            field=models.SlugField(
                default="default", max_length=200, verbose_name="Ссылка"
            ),
            preserve_default=False,
        ),
    ]
