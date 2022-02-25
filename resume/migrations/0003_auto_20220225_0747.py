# Generated by Django 3.2.12 on 2022-02-25 07:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('resume', '0002_auto_20220225_0712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='general_tags',
            field=models.ManyToManyField(blank=True, to='resume.GeneralTag'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='reference',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='resume_reference', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='resume',
            name='skill_tags',
            field=models.ManyToManyField(blank=True, to='resume.SkillTag'),
        ),
    ]