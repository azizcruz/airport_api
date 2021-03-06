# Generated by Django 2.2 on 2019-04-11 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airport_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AirportInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ident', models.CharField(max_length=20)),
                ('type', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=255)),
                ('latitude_deg', models.FloatField()),
                ('longitude_deg', models.FloatField()),
                ('elevation_ft', models.CharField(blank=True, max_length=30, null=True)),
                ('continent', models.CharField(max_length=2)),
                ('iso_country', models.CharField(max_length=2)),
                ('iso_region', models.CharField(max_length=10)),
                ('municipality', models.CharField(max_length=255)),
                ('scheduled_service', models.BooleanField()),
                ('gps_code', models.CharField(blank=True, max_length=10, null=True)),
                ('iata_code', models.CharField(blank=True, max_length=255, null=True)),
                ('local_code', models.CharField(blank=True, max_length=255, null=True)),
                ('home_link', models.URLField(blank=True, null=True)),
                ('wikipedia_link', models.URLField(blank=True, null=True)),
                ('keywords', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='AirporInfo',
        ),
    ]
