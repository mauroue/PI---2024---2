# Generated by Django 5.1.1 on 2024-09-28 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_files'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='address',
        ),
        migrations.RemoveField(
            model_name='visa',
            name='user',
        ),
        migrations.RemoveField(
            model_name='user',
            name='visa',
        ),
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.DeleteModel(
            name='Visa',
        ),
    ]
