# Generated by Django 5.1.1 on 2024-09-28 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_files_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.CharField(default='new', max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='worker',
            field=models.BooleanField(default=True),
        ),
    ]
