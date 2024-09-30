from django.db import models

# Create your models here.

class Course(models.Model):
    course_name = models.CharField(max_length=255)
    course_image = models.ImageField(upload_to='courses/')  # Ensure you have Pillow installed
    description = models.TextField()
    course_content = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.DurationField(help_text="Enter the duration of the course (in HH:MM:SS format).")
    language = models.CharField(max_length=100)
    skill_level = models.CharField(max_length=50, choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced')])
    last_updated = models.DateTimeField(auto_now=True)  # Automatically set to now every time the object is saved
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.course_name

    
class Blog(models.Model):
    blog_title = models.CharField(max_length=255)
    blog_image = models.ImageField(upload_to='blogs/')  # Ensure you have Pillow installed
    blog_data = models.TextField()

    def __str__(self):
        return self.blog_title


class Leads(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)  # Adjust max_length as needed
    email = models.EmailField()
    payment_status = models.BooleanField(default=False)  # True or False

    def __str__(self):
        return self.name
