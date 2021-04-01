# Generated by Django 3.1.7 on 2021-03-31 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_model', models.CharField(max_length=100)),
                ('car_owner', models.CharField(max_length=200)),
                ('car_notes', models.CharField(max_length=200)),
                ('car_number', models.CharField(max_length=200)),
                ('descriptions', models.TextField()),
                ('service_type', models.CharField(blank=True, choices=[('p', 'platinum'), ('g', 'gold')], max_length=1)),
                ('submission_date', models.DateTimeField()),
                ('year_old', models.IntegerField(null=True)),
                ('servicing', models.ManyToManyField(blank=True, to='services.Service')),
            ],
        ),
    ]