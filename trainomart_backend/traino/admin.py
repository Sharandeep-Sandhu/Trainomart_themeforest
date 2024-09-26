from django.contrib import admin
from .models import Course, Blog, Leads

class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'price', 'duration', 'last_updated')  # Display 'last_updated' here
    list_filter = ('language', 'skill_level')
    search_fields = ('course_name', 'description')
    ordering = ('last_updated',)
    fields = ('course_name', 'course_image', 'description', 'course_content', 'price', 'duration', 'language', 'skill_level')  # Exclude 'last_updated' from here

class BlogAdmin(admin.ModelAdmin):
    list_display = ('blog_title', 'blog_image')
    search_fields = ('blog_title',)
    ordering = ('blog_title',)
    fields = ('blog_title', 'blog_image', 'blog_data')

class LeadsAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email', 'payment_status')
    list_filter = ('payment_status',)
    search_fields = ('name', 'email')
    ordering = ('name',)
    fields = ('name', 'phone_number', 'email', 'payment_status')

# Register the models with their corresponding admin classes
admin.site.register(Course, CourseAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Leads, LeadsAdmin)
