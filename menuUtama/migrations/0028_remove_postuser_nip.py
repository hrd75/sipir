# Generated by Django 5.2.1 on 2025-05-30 03:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menuUtama', '0027_postdata_waktu_postuser_nip_alter_postdata_ruangan'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postuser',
            name='NIP',
        ),
    ]
