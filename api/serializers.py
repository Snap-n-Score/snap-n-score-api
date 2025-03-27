from rest_framework import serializers
from .models import Course, User, UserCourse, Faculty, Key, AttendanceStudent

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['course_id', 'course_name']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'username', 'enrollment_id', 'profile_pic', 'courses']

class UserCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCourse
        fields = ['user', 'course']

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = ['faculty_id', 'name', 'course']

class KeySerializer(serializers.ModelSerializer):
    class Meta:
        model = Key
        fields = ['key_id', 'key_value', 'generate_time', 'expire_time', 
                 'public_enkey', 'private_enkey', 'faculty', 'active']

class AttendanceStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceStudent
        fields = ['student', 'key']