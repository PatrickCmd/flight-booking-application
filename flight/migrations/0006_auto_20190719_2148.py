# Generated by Django 2.2.3 on 2019-07-19 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("flight", "0005_reservation")]

    operations = [
        migrations.RemoveField(model_name="reservation", name="seats"),
        migrations.AddField(
            model_name="reservation",
            name="seat",
            field=models.CharField(max_length=5, null=True),
        ),
    ]
