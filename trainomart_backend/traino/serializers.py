from rest_framework import serializers
from .models import Course, Blog, Leads

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leads
        fields = '__all__'
