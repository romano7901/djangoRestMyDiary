# Generated by Django 3.2.7 on 2022-01-10 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mydiaryapp', '0002_schedulerecord'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedulerecord',
            name='recordTimeTo',
            field=models.CharField(max_length=5, null=True),
        ),
    ]
