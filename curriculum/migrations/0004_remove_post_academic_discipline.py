# Generated by Django 4.0.6 on 2022-08-03 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0003_rename_created_date_post_edited_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='academic_discipline',
        ),
    ]
