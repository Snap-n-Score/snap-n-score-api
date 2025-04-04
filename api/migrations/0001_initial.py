# Generated by Django 5.1.6 on 2025-02-14 08:28

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "course_id",
                    models.BigIntegerField(primary_key=True, serialize=False),
                ),
                ("course_name", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                ("user_id", models.BigIntegerField(primary_key=True, serialize=False)),
                ("username", models.CharField(max_length=255)),
                (
                    "enrollment_id",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("profile_pic", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Faculty",
            fields=[
                (
                    "faculty_id",
                    models.BigIntegerField(primary_key=True, serialize=False),
                ),
                ("name", models.CharField(max_length=255)),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.course"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "faculties",
            },
        ),
        migrations.CreateModel(
            name="Key",
            fields=[
                ("key_id", models.BigIntegerField(primary_key=True, serialize=False)),
                ("key_value", models.BigIntegerField()),
                (
                    "generate_time",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("expire_time", models.DateTimeField()),
                ("public_enkey", models.CharField(max_length=255)),
                ("private_enkey", models.CharField(max_length=255)),
                ("active", models.BooleanField(default=True)),
                (
                    "faculty",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.faculty"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserCourse",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.course"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.user"
                    ),
                ),
            ],
            options={
                "unique_together": {("user", "course")},
            },
        ),
        migrations.AddField(
            model_name="user",
            name="courses",
            field=models.ManyToManyField(through="api.UserCourse", to="api.course"),
        ),
        migrations.CreateModel(
            name="AttendanceStudent",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "key",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.key"
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.user"
                    ),
                ),
            ],
            options={
                "unique_together": {("student", "key")},
            },
        ),
    ]
