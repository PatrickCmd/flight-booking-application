# Generated by Django 2.2.3 on 2019-07-17 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("authenticate", "0002_auto_20190715_0044")]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="middle_name",
            field=models.CharField(blank=True, max_length=100, null=True),
        )
    ]
