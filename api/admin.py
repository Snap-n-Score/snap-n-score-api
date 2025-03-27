
from django.contrib import admin
from .models import Course, User, UserCourse, Faculty, Key, AttendanceStudent

admin.site.register(Course)
admin.site.register(User)
admin.site.register(UserCourse)
admin.site.register(Faculty)
admin.site.register(Key)
admin.site.register(AttendanceStudent)