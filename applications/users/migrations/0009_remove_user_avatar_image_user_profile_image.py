# Generated by Django 4.2.5 on 2023-09-21 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_user_avatar_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='avatar_image',
        ),
        migrations.AddField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='users/profileImages'),
        ),
    ]