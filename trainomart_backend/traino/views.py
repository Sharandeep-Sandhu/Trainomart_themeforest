from django.shortcuts import render
from django.http import HttpResponse
from .serializers import CourseSerializer, BlogSerializer, LeadSerializer, StudentsSerializer, ContactMessageSerializer, PaymentSerializer, BusinessLeadsSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Course, Blog, Leads, Students, ContactMessage, Payment, BusinessLeads
from django.shortcuts import get_object_or_404
from rest_framework import filters, status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .wise_service import create_quote, create_transfer
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework import mixins

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

    @action(detail=False, methods=['get'], url_path='limited')
    def get_limited_courses(self, request):
        """Get a limited number of courses using a query parameter 'limit'"""
        limit = request.query_params.get('limit', 5)  # Default to 5 courses
        try:
            limit = int(limit)
        except ValueError:
            return Response({"error": "Invalid limit value"}, status=status.HTTP_400_BAD_REQUEST)
        
        queryset = Course.objects.all().order_by('-id')[:limit]
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'], url_path='custom-get')
    def custom_get_course_by_id(self, request, pk=None):
        """Custom action to fetch course by ID"""
        course = get_object_or_404(Course, pk=pk)
        serializer = CourseSerializer(course)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    @action(detail=False, methods=['get'], url_path='by-name')
    def get_course_by_name(self, request):
        """Get course by name"""
        course_name = request.query_params.get('name', None)
        if course_name:
            # Filtering by course name
            courses = Course.objects.filter(course_name__iexact=course_name)
            if courses.exists():
                serializer = self.get_serializer(courses, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({'error': 'Course not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'error': 'No course name provided'}, status=status.HTTP_400_BAD_REQUEST)

    
    
class BlogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class LeadViewSet(viewsets.ModelViewSet):
    queryset = Leads.objects.all()
    serializer_class = LeadSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer

class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BusinessLeadsViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = BusinessLeads.objects.all()
    serializer_class = BusinessLeadsSerializer

def index(request):
    return HttpResponse("Hello, world. You're at the trainomart index.")
