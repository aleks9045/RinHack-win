# Generated by Django 4.2 on 2023-04-28 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_files_name_files_size_alter_files_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='files',
            name='name',
        ),
        migrations.RemoveField(
            model_name='files',
            name='size',
        ),
    ]
