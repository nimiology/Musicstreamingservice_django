# Generated by Django 4.0 on 2022-01-11 21:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='createDTime',
            new_name='createdTime',
        ),
    ]
