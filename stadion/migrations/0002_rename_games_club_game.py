# Generated by Django 4.2.7 on 2024-04-04 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stadion', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='club',
            old_name='games',
            new_name='game',
        ),
    ]
