# Generated by Django 4.0.3 on 2022-04-15 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Control',
        ),
        migrations.RenameField(
            model_name='control',
            old_name='content',
            new_name='field',
        ),
    ]
