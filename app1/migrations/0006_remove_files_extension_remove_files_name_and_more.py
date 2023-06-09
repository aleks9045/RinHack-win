# Generated by Django 4.2 on 2023-04-28 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_remove_useruser_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='files',
            name='extension',
        ),
        migrations.RemoveField(
            model_name='files',
            name='name',
        ),
        migrations.RemoveField(
            model_name='files',
            name='upload_date',
        ),
        migrations.RemoveField(
            model_name='files',
            name='weight',
        ),
        migrations.AddField(
            model_name='files',
            name='file',
            field=models.FileField(default=1, upload_to='media ', verbose_name='file'),
            preserve_default=False,
        ),
    ]
