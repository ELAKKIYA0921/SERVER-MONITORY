# Generated by Django 3.0.4 on 2022-06-18 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BostonV1_app', '0002_auto_20220618_1422'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cpu_data',
            old_name='cpu_id',
            new_name='server_data',
        ),
        migrations.RemoveField(
            model_name='cpu_data',
            name='Time',
        ),
    ]
