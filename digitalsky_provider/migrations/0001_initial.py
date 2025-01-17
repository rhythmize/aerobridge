# Generated by Django 3.2.9 on 2022-01-05 11:58

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gcs_operations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DigitalSkyLog',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('response_code', models.CharField(max_length=256)),
                ('response', models.TextField(default='Raw response from DGCA Digital Sky Server is stored here.')),
                ('timestamp', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('txn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gcs_operations.transaction')),
            ],
        ),
    ]
