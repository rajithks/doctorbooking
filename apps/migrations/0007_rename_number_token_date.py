# Generated by Django 4.1.5 on 2023-05-19 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0006_alter_message_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='token',
            old_name='number',
            new_name='date',
        ),
    ]
