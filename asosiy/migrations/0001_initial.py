# Generated by Django 4.1.3 on 2023-04-17 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('file', models.FileField(null=True, upload_to='audios')),
                ('rn', models.PositiveIntegerField(default=1)),
                ('duration', models.DurationField(blank=True, null=True)),
                ('size', models.FloatField(blank=True, null=True)),
                ('topic', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='asosiy.topic')),
            ],
        ),
    ]
