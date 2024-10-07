from django.contrib import admin
from .models import Course, Blog, Leads, Students, ContactMessage

class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'you_will_learn_list', 'orignal_price', 'price', 'duration', 'is_featured', 'last_updated')
    list_filter = ('is_featured', 'language', 'skill_level')
    search_fields = ('course_name', 'description')
    ordering = ('last_updated',)
    fields = (
        'course_name',
        'course_image',
        'description',
        'course_content',
        'you_will_learn_list',  # Update this line
        'Lessons',
        'Requirements',
        'category',
        'price',
        'orignal_price',
        'duration',
        'language',
        'skill_level',
        'is_featured',
    )

class BlogAdmin(admin.ModelAdmin):
    list_display = ('blog_title', 'blog_image')
    search_fields = ('blog_title',)
    ordering = ('blog_title',)
    fields = ('blog_title', 'blog_image', 'blog_data')

class StudentsAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'student_mail', 'student_phone')
    search_fields = ('student_name',)
    ordering = ('student_name',)
    fields = ('student_name', 'student_mail', 'student_phone')
class LeadsAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email', 'payment_status')
    list_filter = ('payment_status',)
    search_fields = ('name', 'email')
    ordering = ('name',)
    fields = ('name', 'phone_number', 'email', 'payment_status')


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')  # Fields to display in the list view
    search_fields = ('name', 'email')  # Fields to enable searching
    list_filter = ('created_at',)  # Enable filtering by created date
    ordering = ('-created_at',)  # Order by created date descending
    

# Register the models with their corresponding admin classes
admin.site.register(Course, CourseAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Leads, LeadsAdmin)
admin.site.register(Students, StudentsAdmin)

