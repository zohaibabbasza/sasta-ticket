# Generated by Django 3.2.12 on 2022-02-25 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SkillTags',
            new_name='GeneralTag',
        ),
        migrations.RenameModel(
            old_name='GeneralTags',
            new_name='SkillTag',
        ),
    ]
