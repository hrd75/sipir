# Generated by Django 5.2.1 on 2025-05-28 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menuUtama', '0023_remove_postuser_nip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postdata',
            name='nama',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='postdata',
            name='satker',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.DeleteModel(
            name='PostUser',
        ),
    ]
