# Generated by Django 2.2.3 on 2019-07-18 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("profiles", "0001_initial")]

    operations = [
        migrations.AlterField(
            model_name="passportinfo",
            name="expiration_date",
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name="passportinfo",
            name="issue_date",
            field=models.DateField(null=True),
        ),
    ]
