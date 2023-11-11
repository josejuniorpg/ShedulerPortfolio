# Generated by Django 4.2.7 on 2023-11-11 03:22

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shifts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MissingHours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('daily_scheduler', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shifts.dailyscheduler')),
                ('missing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shifts.missing')),
                ('scheduler', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shifts.scheduler')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
