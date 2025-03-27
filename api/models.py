from django.db import models
from django.utils import timezone

class Course(models.Model):
    course_id = models.BigIntegerField(primary_key=True)
    course_name = models.TextField()

    def __str__(self):
        return self.course_name

class User(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    username = models.CharField(max_length=255)
    enrollment_id = models.CharField(max_length=255, null=True, blank=True)
    profile_pic = models.TextField(null=True, blank=True)
    courses = models.ManyToManyField(Course, through='UserCourse')

    def __str__(self):
        return self.username

class UserCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['user', 'course']

class Faculty(models.Model):
    faculty_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "faculties"

class Key(models.Model):
    key_id = models.BigIntegerField(primary_key=True)
    key_value = models.BigIntegerField()
    generate_time = models.DateTimeField(default=timezone.now)
    expire_time = models.DateTimeField()
    public_enkey = models.CharField(max_length=255)
    private_enkey = models.CharField(max_length=255)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"Key {self.key_id}"

class AttendanceStudent(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    key = models.ForeignKey(Key, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['student', 'key']

    def __str__(self):
        return f"Attendance: {self.student.username} - Key {self.key.key_id}"