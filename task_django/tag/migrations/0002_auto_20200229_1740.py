# Generated by Django 2.2 on 2020-02-29 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='task',
            new_name='tasks',
        ),
    ]
