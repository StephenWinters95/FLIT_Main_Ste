# Generated by Django 4.2.7 on 2024-12-09 07:19

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import fp_courses.models


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
                ('disp_seq', models.IntegerField(default=10)),
                ('course_code', models.IntegerField(primary_key=True, serialize=False)),
                ('version', models.CharField(max_length=3)),
                ('title', models.CharField(max_length=200)),
                ('subtitle', models.CharField(max_length=200)),
                ('featured_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('effective_from', models.DateField(auto_now_add=True)),
                ('effective_to', models.DateField(default=fp_courses.models.today_plus_10_years)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('updated_on', models.DateField(auto_now=True)),
                ('status', models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=0)),
                ('author', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, related_name='courses', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['disp_seq', 'course_code', 'version'],
                'unique_together': {('course_code', 'version')},
            },
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('quiz_code', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('question_text', models.CharField(default='Question text goes here?', max_length=200)),
                ('ans1_text', models.CharField(default='Answer1 goes here', max_length=200)),
                ('ans2_text', models.CharField(default='Answer2 goes here', max_length=200)),
                ('ans3_text', models.CharField(default='Answer3 goes here', max_length=200)),
                ('ans4_text', models.CharField(default='Answer4 goes here', max_length=200)),
                ('correct_ans', models.IntegerField()),
                ('explanation', models.CharField(default='Correct answer is X:  This is because ......', max_length=300)),
                ('updated_on', models.DateField(auto_now=True)),
                ('status', models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=0)),
                ('author', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, related_name='quiz', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['quiz_code'],
            },
        ),
        migrations.CreateModel(
            name='Cohort',
            fields=[
                ('cohort_code', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200, unique=True)),
                ('subtitle', models.CharField(max_length=200, unique=True)),
                ('featured_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('effective_from', models.DateField(default=fp_courses.models.today_date)),
                ('effective_to', models.DateField(default=fp_courses.models.today_plus_one_year)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('updated_on', models.DateField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=0)),
                ('author', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, related_name='admin_cohorts', to=settings.AUTH_USER_MODEL)),
                ('members', models.ManyToManyField(blank=True, related_name='cohort_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['cohort_code'],
            },
        ),
        migrations.CreateModel(
            name='CourseContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(max_length=3)),
                ('seq_num', models.IntegerField(default=10)),
                ('content_type', models.IntegerField(choices=[(0, 'Article'), (1, 'Quiz')], default=0)),
                ('status', models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=0)),
                ('article', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, related_name='course_article', to='fp_blog.article')),
                ('course_code', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, related_name='course_contents', to='fp_courses.course')),
            ],
            options={
                'ordering': ['course_code', 'version', 'seq_num'],
                'unique_together': {('course_code', 'version', 'seq_num')},
            },
        ),
    ]
