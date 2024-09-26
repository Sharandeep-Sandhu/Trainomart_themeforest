from django.shortcuts import render
from django.http import HttpResponse
from .serializers import CourseSerializer, BlogSerializer, LeadSerializer
from rest_framework import viewsets
from .models import Course, Blog, Leads

# Create your views here.

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class LeadViewSet(viewsets.ModelViewSet):
    queryset = Leads.objects.all()
    serializer_class = LeadSerializer
    
def index(request):
    return HttpResponse("Hello, world. You're at the trainomart index.")