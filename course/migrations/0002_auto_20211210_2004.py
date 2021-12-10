# Generated by Django 2.2.6 on 2021-12-10 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("course", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "course_name",
                    models.CharField(
                        blank=True, max_length=90, null=True, verbose_name="课程名称"
                    ),
                ),
                (
                    "course_introduction",
                    models.TextField(blank=True, verbose_name="课程简介"),
                ),
                ("teacher", models.CharField(max_length=90, verbose_name="教师姓名")),
                ("create_people", models.CharField(max_length=90, verbose_name="创建人")),
                (
                    "manage_student",
                    models.TextField(blank=True, null=True, verbose_name="学生管理员"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserCourseContact",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("course_id", models.IntegerField(verbose_name="课程id")),
            ],
        ),
        migrations.DeleteModel(
            name="CourseConnect",
        ),
        migrations.DeleteModel(
            name="CourseTable",
        ),
    ]
