# Generated by Django 2.2.3 on 2019-07-18 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(blank=True, max_length=10, null=True)),
                ('is_available', models.BooleanField(default=True)),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seats', to='flight.Flight')),
            ],
        ),
    ]