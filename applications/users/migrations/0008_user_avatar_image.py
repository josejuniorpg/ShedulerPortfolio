# Generated by Django 4.2.5 on 2023-09-21 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_rename_phone_umber_user_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar_image',
            field=models.ImageField(blank=True, null=True, upload_to='users/avatarImages'),
        ),
    ]
