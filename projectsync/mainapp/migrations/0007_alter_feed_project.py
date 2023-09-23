# Generated by Django 4.2.5 on 2023-09-23 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0006_follow"),
    ]

    operations = [
        migrations.AlterField(
            model_name="feed",
            name="project",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="mainapp.project",
            ),
        ),
    ]
