from django.shortcuts import render
from django.http import HttpResponse
from .serializers import CourseSerializer, BlogSerializer, LeadSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Course, Blog, Leads
from rest_framework import filters

# Create your views here.

class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['course_name']  # Allows search by course name
    
    @action(detail=False, methods=['get'])
    def featured(self, request):
        """Filter courses by whether they are featured"""
        featured_courses = Course.objects.filter(is_featured=True)
        serializer = self.get_serializer(featured_courses, many=True)
        return Response(serializer.data)

class BlogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class LeadViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Leads.objects.all()
    serializer_class = LeadSerializer

def index(request):
    return HttpResponse("Hello, world. You're at the trainomart index.")
