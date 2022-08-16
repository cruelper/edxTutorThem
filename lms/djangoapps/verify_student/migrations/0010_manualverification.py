# Generated by Django 1.11.13 on 2018-06-07 10:51


import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('verify_student', '0009_remove_id_verification_aggregate'),
    ]

    operations = [
        migrations.CreateModel(
            name='ManualVerification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', model_utils.fields.StatusField(choices=[('created', 'created'), ('ready', 'ready'), ('submitted', 'submitted'), ('must_retry', 'must_retry'), ('approved', 'approved'), ('denied', 'denied')], default='created', max_length=100, no_check_for_status=True, verbose_name='status')),
                ('status_changed', model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor='status', verbose_name='status changed')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('reason', models.CharField(blank=True, help_text='Specifies the reason for manual verification of the user.', max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
