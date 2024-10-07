from rest_framework import serializers
from .models import Course, Blog, Leads, Students, ContactMessage

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'course_name', 'course_image', 'course_content', 'description', 'you_will_learn_list', 'Lessons', 'Requirements', 'category', 'duration', 'language', 'skill_level', 'price', 'orignal_price', 'last_updated', 'is_featured']


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
        
class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        
class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leads
        fields = '__all__'

class PaymentSerializer(serializers.Serializer):
    user_email = serializers.EmailField()
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    currency = serializers.CharField(max_length=10)