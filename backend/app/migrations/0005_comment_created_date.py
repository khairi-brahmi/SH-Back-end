# Generated by Django 3.0.5 on 2021-02-20 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20210219_2054'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
