# Generated by Django 2.2.3 on 2019-07-18 14:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('origin', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100)),
                ('departure', models.DateTimeField()),
                ('arrival', models.DateTimeField()),
                ('aircraft', models.DateTimeField()),
                ('status', models.CharField(choices=[('DELAYED', 'DELAYED'), ('ON_TIME', 'ON_TIME'), ('ARRIVED', 'ARRIVED'), ('LATE', 'LATE')], max_length=10)),
                ('number', models.CharField(max_length=100)),
                ('capacity', models.IntegerField()),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flights', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
