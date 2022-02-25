# Generated by Django 3.2.12 on 2022-02-25 09:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('resume', '0003_auto_20220225_0747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='resume_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
