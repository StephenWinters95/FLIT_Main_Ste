# Generated by Django 4.2.7 on 2024-11-09 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fp_personal', '0018_alter_useraction_parent_article_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='family_size',
            field=models.PositiveIntegerField(default='1'),
            preserve_default=False,
        ),
    ]
