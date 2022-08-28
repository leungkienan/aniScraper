# Generated by Django 4.1 on 2022-08-28 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='anime',
            old_name='epiNum',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='anime',
            old_name='downloadLink',
            new_name='malLink',
        ),
        migrations.RemoveField(
            model_name='anime',
            name='seasonAired',
        ),
        migrations.AddField(
            model_name='anime',
            name='url',
            field=models.CharField(default=None, max_length=2048),
            preserve_default=False,
        ),
    ]