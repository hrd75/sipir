# Generated by Django 5.2.1 on 2025-06-04 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menuUtama', '0032_postuser_ruangan_postuser_satker'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postuser',
            name='ruangan',
        ),
    ]
