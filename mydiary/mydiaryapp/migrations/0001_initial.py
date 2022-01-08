# Generated by Django 3.2.7 on 2021-12-22 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('creator', models.IntegerField(default=12345)),
                ('isDeleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='DiaryNote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=90)),
                ('desc', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patientId', models.IntegerField()),
                ('fullName', models.CharField(max_length=200)),
                ('birthDate', models.CharField(max_length=10)),
                ('policy', models.CharField(max_length=30)),
                ('lpuId', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resourceId', models.IntegerField()),
                ('doctorId', models.IntegerField()),
                ('doctorName', models.CharField(max_length=255)),
                ('specialityId', models.IntegerField()),
                ('specialityName', models.CharField(max_length=255)),
                ('duration', models.IntegerField()),
                ('cabNum', models.CharField(max_length=25)),
                ('timeAvail', models.CharField(max_length=255)),
                ('timeUnavail', models.CharField(max_length=255)),
                ('maskAvail', models.CharField(max_length=20)),
                ('maskUnavail', models.CharField(max_length=20)),
                ('comment', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.IntegerField(default=54321)),
                ('text', models.CharField(max_length=500)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('conversation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mydiaryapp.conversation')),
            ],
        ),
        migrations.CreateModel(
            name='DiaryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s3key', models.CharField(max_length=255)),
                ('s3url', models.CharField(blank=True, max_length=255)),
                ('diarynote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='mydiaryapp.diarynote')),
            ],
        ),
    ]
