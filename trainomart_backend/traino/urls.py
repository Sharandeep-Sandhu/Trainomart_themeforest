from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, BlogViewSet, LeadViewSet
from . import views

router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'blogs', BlogViewSet)
router.register(r'leads', LeadViewSet)


urlpatterns = [
    path("", views.index, name="index"),
    path('api/', include(router.urls)),
]