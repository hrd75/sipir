# Generated by Django 5.2.1 on 2025-06-12 06:22

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menuUtama', '0053_remove_postdata_pukul_remove_postdata_tanggal_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postdata',
            name='waktu',
            field=models.DateTimeField(verbose_name=django.utils.timezone.now),
        ),
    ]
