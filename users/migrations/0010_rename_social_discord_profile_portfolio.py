# Generated by Django 4.2.6 on 2024-02-27 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_profile_profile_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='social_discord',
            new_name='portfolio',
        ),
    ]
