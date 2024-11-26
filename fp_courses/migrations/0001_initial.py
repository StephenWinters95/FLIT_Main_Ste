# Generated by Django 4.2.7 on 2024-11-25 22:00

import cloudinary.models
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fp_blog', '0014_survey'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_code', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('version', models.CharField(max_length=3)),
                ('title', models.CharField(max_length=200)),
                ('subtitle', models.CharField(max_length=200)),
                ('featured_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('effective_from', models.DateTimeField(auto_now_add=True)),
                ('effective_to', models.DateTimeField(default=datetime.datetime(2034, 11, 25, 21, 59, 59, 975344))),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=0)),
                ('author', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, related_name='courses', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['course_code', 'version'],
                'unique_together': {('course_code', 'version')},
            },
        ),
        migrations.CreateModel(
            name='Cohort',
            fields=[
                ('cohort_code', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200, unique=True)),
                ('subtitle', models.CharField(max_length=200, unique=True)),
                ('featured_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('effective_from', models.DateTimeField(auto_now_add=True)),
                ('effective_to', models.DateTimeField(default=datetime.datetime(2025, 11, 25, 21, 59, 59, 976424))),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=0)),
                ('author', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, related_name='admin_cohorts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['cohort_code'],
            },
        ),
        migrations.CreateModel(
            name='CourseContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seq_num', models.IntegerField(default=10)),
                ('content_type', models.IntegerField(choices=[(0, 'Article'), (1, 'Quiz')], default=0)),
                ('status', models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=0)),
                ('article', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, related_name='course_article', to='fp_blog.article')),
                ('course_code', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, related_name='contents', to='fp_courses.course')),
                ('version', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='version_contents', to='fp_courses.course')),
            ],
            options={
                'ordering': ['course_code', 'version', 'seq_num'],
                'unique_together': {('course_code', 'version', 'seq_num')},
            },
        ),
    ]