# Generated by Django 5.2.1 on 2025-05-20 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namaPeminjam', models.CharField(max_length=200)),
                ('satkerPeminjam', models.CharField(max_length=200)),
                ('ruangan', models.TextField()),
                ('waktu', models.DateTimeField()),
                ('keterangan', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
