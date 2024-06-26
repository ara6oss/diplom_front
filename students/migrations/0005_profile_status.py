# Generated by Django 4.2.7 on 2024-06-04 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("students", "0004_alter_profile_options_remove_profile_first_name_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="status",
            field=models.CharField(
                choices=[("student", "Student"), ("teacher", "Teacher")],
                default="student",
                max_length=7,
            ),
        ),
    ]
