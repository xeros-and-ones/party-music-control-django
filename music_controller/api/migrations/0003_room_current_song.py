# Generated by Django 4.2.7 on 2023-12-03 12:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0002_alter_room_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="room",
            name="current_song",
            field=models.CharField(max_length=50, null=True),
        ),
    ]
