# Generated by Django 3.2.5 on 2021-08-31 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('companyname', models.CharField(max_length=50)),
                ('startdate', models.DateField(blank=True)),
                ('enddate', models.DateField(blank=True)),
                ('companydescription', models.CharField(max_length=350)),
                ('jobdescription', models.CharField(max_length=2550)),
                ('url', models.URLField(blank=True)),
            ],
        ),
    ]
