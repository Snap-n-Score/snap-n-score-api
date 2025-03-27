from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import (CourseViewSet, UserViewSet, UserCourseViewSet,
                   FacultyViewSet, KeyViewSet, AttendanceStudentViewSet)

router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'users', UserViewSet)
router.register(r'user-courses', UserCourseViewSet)
router.register(r'faculty', FacultyViewSet)
router.register(r'keys', KeyViewSet)
router.register(r'attendance', AttendanceStudentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]