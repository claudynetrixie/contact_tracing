# Generated by Django 3.1 on 2020-08-23 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_tracing', '0008_auto_20200822_0138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='infectionreport',
            name='date_recorded',
        ),
        migrations.AlterField(
            model_name='infectionreport',
            name='time_recorded',
            field=models.DateTimeField(),
        ),
    ]
