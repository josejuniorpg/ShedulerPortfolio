# Generated by Django 4.2.5 on 2023-09-21 00:15

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_user_code_verification_alter_user_gender_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone_umber',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None),
        ),
    ]