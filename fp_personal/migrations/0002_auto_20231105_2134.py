# Generated by Django 3.2.22 on 2023-11-05 21:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fp_personal', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useraction',
            old_name='action_desc',
            new_name='user_action_desc',
        ),
        migrations.RenameField(
            model_name='useraction',
            old_name='action_taken',
            new_name='user_action_taken',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='name',
        ),
    ]
