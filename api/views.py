from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Course, User, UserCourse, Faculty, Key, AttendanceStudent
from .serializers import (CourseSerializer, UserSerializer, UserCourseSerializer,
                        FacultySerializer, KeySerializer, AttendanceStudentSerializer)

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    # permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['get'])
    def enrolled_students(self, request, pk=None):
        course = self.get_object()
        students = User.objects.filter(courses=course)
        serializer = UserSerializer(students, many=True)
        return Response(serializer.data)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]
# 
    @action(detail=True, methods=['get'])
    def courses(self, request, pk=None):
        user = self.get_object()
        courses = user.courses.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def enroll(self, request, pk=None):
        user = self.get_object()
        course_id = request.data.get('course_id')
        course = get_object_or_404(Course, pk=course_id)
        UserCourse.objects.create(user=user, course=course)
        return Response({'status': 'enrolled'})

class UserCourseViewSet(viewsets.ModelViewSet):
    queryset = UserCourse.objects.all()
    serializer_class = UserCourseSerializer
    # permission_classes = [permissions.IsAuthenticated]

class FacultyViewSet(viewsets.ModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    # permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['get'])
    def active_keys(self, request, pk=None):
        faculty = self.get_object()
        keys = Key.objects.filter(faculty=faculty, active=True)
        serializer = KeySerializer(keys, many=True)
        return Response(serializer.data)

class KeyViewSet(viewsets.ModelViewSet):
    queryset = Key.objects.all()
    serializer_class = KeySerializer
    # permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['get'])
    def attendance_list(self, request, pk=None):
        key = self.get_object()
        attendance = AttendanceStudent.objects.filter(key=key)
        serializer = AttendanceStudentSerializer(attendance, many=True)
        return Response(serializer.data)

class AttendanceStudentViewSet(viewsets.ModelViewSet):
    queryset = AttendanceStudent.objects.all()
    serializer_class = AttendanceStudentSerializer
    # permission_classes = [permissions.IsAuthenticated]