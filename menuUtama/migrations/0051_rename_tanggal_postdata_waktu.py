# Generated by Django 5.2.1 on 2025-06-12 04:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menuUtama', '0050_remove_postdata_pukul'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postdata',
            old_name='tanggal',
            new_name='waktu',
        ),
    ]
