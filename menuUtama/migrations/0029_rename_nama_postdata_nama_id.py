# Generated by Django 5.2.1 on 2025-05-30 03:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menuUtama', '0028_remove_postuser_nip'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postdata',
            old_name='nama',
            new_name='nama_id',
        ),
    ]
