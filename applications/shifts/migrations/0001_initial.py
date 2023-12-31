# Generated by Django 4.2.7 on 2023-11-11 07:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Assistance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_vacations', models.BooleanField(default=False)),
                ('date', models.DateField()),
                ('has_assisted', models.PositiveSmallIntegerField(choices=[(0, 'did not assist'), (1, 'assisted '), (2, 'assisted but left early'), (4, 'arrived late'), (5, 'arrived late and left early')], default=0)),
            ],
            options={
                'verbose_name': 'Assistance',
                'verbose_name_plural': 'Assistances',
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='JustificationCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=50)),
            ],
            options={
                'verbose_name': 'Justification Category',
                'verbose_name_plural': 'Justification Categories',
                'db_table': 'shifts_justification_category',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='MissingCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=50)),
            ],
            options={
                'verbose_name': 'Missing Category',
                'verbose_name_plural': 'Missing Categories',
                'db_table': 'shifts_missing_category',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Scheduler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('status', models.BooleanField(default=True)),
                ('description', models.CharField(blank=True, max_length=50)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
            options={
                'verbose_name': 'Scheduler',
                'verbose_name_plural': 'Schedulers',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_temporal', models.BooleanField(default=False)),
                ('duration', models.PositiveSmallIntegerField()),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Shift',
                'verbose_name_plural': 'Shifts',
                'ordering': ['-user', '-created'],
            },
        ),
        migrations.CreateModel(
            name='ShiftCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=50)),
            ],
            options={
                'verbose_name': 'Shift Category',
                'verbose_name_plural': 'Shift Categories',
                'db_table': 'shifts_shift_category',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='ShiftDaily',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('status', models.BooleanField(default=True)),
                ('description', models.CharField(blank=True, max_length=50)),
                ('day_of_the_week', models.PositiveSmallIntegerField(choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday')])),
                ('group', models.CharField(blank=True, max_length=50)),
                ('shift', models.ForeignKey(limit_choices_to={'status': True}, on_delete=django.db.models.deletion.CASCADE, to='shifts.shift')),
                ('shift_schedulers', models.ManyToManyField(limit_choices_to={'status': True}, to='shifts.scheduler')),
            ],
            options={
                'verbose_name': 'Shift Daily',
                'verbose_name_plural': 'Shifts Daily',
                'db_table': 'shifts_shift_daily',
                'ordering': ['-day_of_the_week', '-created'],
                'unique_together': {('shift', 'day_of_the_week')},
            },
        ),
        migrations.AddField(
            model_name='shift',
            name='shift_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shifts.shiftcategory'),
        ),
        migrations.AddField(
            model_name='shift',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Missing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_justified', models.BooleanField(default=False)),
                ('reason', models.CharField(blank=True, max_length=50)),
                ('worked_hours', models.PositiveSmallIntegerField(default=0)),
                ('assistance', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='shifts.assistance')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shifts.missingcategory')),
                ('missing_hours', models.ManyToManyField(to='shifts.scheduler')),
            ],
            options={
                'verbose_name': 'Missing',
                'verbose_name_plural': 'Missings',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Justification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('status', models.BooleanField(default=True)),
                ('description', models.CharField(blank=True, max_length=50)),
                ('document', models.FileField(blank=True, null=True, upload_to='shifts/justificationsDocuments')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shifts.justificationcategory')),
                ('missing', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='shifts.missing')),
            ],
            options={
                'verbose_name': 'Justification',
                'verbose_name_plural': 'Justifications',
                'ordering': ['-created'],
            },
        ),
        migrations.AddField(
            model_name='assistance',
            name='daily_scheduler',
            field=models.ForeignKey(limit_choices_to={'status': True}, on_delete=django.db.models.deletion.CASCADE, to='shifts.shiftdaily'),
        ),
        migrations.AlterUniqueTogether(
            name='assistance',
            unique_together={('daily_scheduler', 'date')},
        ),
    ]
