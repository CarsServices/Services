# Generated by Django 5.0.3 on 2024-07-07 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Address_1', models.CharField(blank=True, max_length=120)),
                ('city', models.CharField(max_length=110)),
            ],
        ),
    ]
