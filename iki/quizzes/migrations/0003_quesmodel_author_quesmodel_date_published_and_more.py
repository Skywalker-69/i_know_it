# Generated by Django 4.1.3 on 2022-11-18 18:47

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quizzes', '0002_quesmodel_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='quesmodel',
            name='author',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='author'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quesmodel',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 18, 18, 47, 7, 495670, tzinfo=datetime.timezone.utc), verbose_name='date published'),
        ),
        migrations.AddField(
            model_name='quesmodel',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='is published'),
        ),
    ]