# Generated by Django 5.2.1 on 2025-05-22 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inputNama', models.CharField(max_length=50)),
                ('inputSatker', models.CharField(max_length=25)),
                ('choiceRuangan', models.CharField(max_length=200)),
                ('waktuPinjam', models.DateTimeField()),
                ('inputKeterangan', models.TextField()),
            ],
        ),
    ]
