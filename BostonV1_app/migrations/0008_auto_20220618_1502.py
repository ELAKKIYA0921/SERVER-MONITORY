# Generated by Django 3.0.4 on 2022-06-18 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BostonV1_app', '0007_auto_20220618_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cpu_data',
            name='server_data',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='BostonV1_app.Server_Data', verbose_name='server'),
        ),
    ]