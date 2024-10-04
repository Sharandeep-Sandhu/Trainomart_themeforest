from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, BlogViewSet, LeadViewSet, StudentsViewSet, ContactMessageViewSet
from . import views

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='course')
router.register(r'blogs', BlogViewSet, basename='blog')
# router.register(r'leads', LeadViewSet, basename='lead')
router.register(r'leads', LeadViewSet)
router.register(r'students', StudentsViewSet, basename='students')
router.register(r'contact', ContactMessageViewSet)



urlpatterns = [
    path("", views.index, name="index"),
    path('api/', include(router.urls)),
]