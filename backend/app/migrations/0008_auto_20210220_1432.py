# Generated by Django 3.0.5 on 2021-02-20 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20210220_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savepost',
            name='savedby',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='saved', to='app.SimpleUser'),
        ),
    ]
