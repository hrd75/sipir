# Generated by Django 5.2.1 on 2025-06-12 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menuUtama', '0048_rename_waktu_postdata_pukul_postdata_tanggal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postdata',
            name='pukul',
            field=models.TimeField(),
        ),
    ]
