# Generated by Django 4.2.7 on 2024-12-02 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fp_courses', '0012_alter_cohort_effective_from'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_code',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='course',
            name='updated_on',
            field=models.DateField(auto_now=True),
        ),
    ]
