# Generated by Django 4.2.11 on 2025-04-20 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fire', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('contact', models.CharField(max_length=20)),
            ],
        ),
    ]
