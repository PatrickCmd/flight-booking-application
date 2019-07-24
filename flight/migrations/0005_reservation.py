# Generated by Django 2.2.3 on 2019-07-19 12:17

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("flight", "0004_auto_20190719_0900"),
    ]

    operations = [
        migrations.CreateModel(
            name="Reservation",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "seats",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=5), blank=True, size=None
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("ACTIVE", "ACTIVE"), ("CANCELLED", "CANCELLED")],
                        default="ACTIVE",
                        max_length=10,
                    ),
                ),
                ("is_cancelled", models.BooleanField(default=False)),
                ("reserved_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "flight",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reservations",
                        to="flight.Flight",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reservations",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        )
    ]
