# Generated by Django 5.2.1 on 2025-06-12 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menuUtama', '0044_alter_postdata_keterangan_alter_postdata_waktu'),
    ]

    operations = [
        migrations.AddField(
            model_name='postdata',
            name='pukul',
            field=models.TimeField(default=0),
            preserve_default=False,
        ),
    ]
