# Generated by Django 4.2.5 on 2023-09-21 00:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_remove_user_avatar_image_user_profile_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['-created'], 'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
    ]
