# Generated by Django 4.2.7 on 2024-11-26 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fp_courses', '0009_cohort_members_alter_cohort_created_on_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CohortUser',
        ),
    ]
