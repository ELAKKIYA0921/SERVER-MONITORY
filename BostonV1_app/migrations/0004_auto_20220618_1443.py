# Generated by Django 3.0.4 on 2022-06-18 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BostonV1_app', '0003_auto_20220618_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cpu_data',
            name='server_data',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BostonV1_app.Server_Data', verbose_name='server'),
        ),
    ]
