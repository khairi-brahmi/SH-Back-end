# Generated by Django 3.0.5 on 2021-02-19 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210219_1935'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportPost',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('postID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reports', to='app.Post')),
                ('reportedby', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reported', to='app.SimpleUser')),
            ],
        ),
        migrations.DeleteModel(
            name='SharePost',
        ),
    ]