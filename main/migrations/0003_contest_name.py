# Generated by Django 4.1.6 on 2023-02-16 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_points'),
    ]

    operations = [
        migrations.AddField(
            model_name='contest',
            name='name',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]