from django.db import models

# Create your models here.

class Course(models.Model):
    course_name = models.CharField(max_length=255)
    course_image = models.ImageField(upload_to='courses/')  # Ensure you have Pillow installed
    description = models.TextField(max_length=500000)
    course_content = models.TextField(max_length=500000)
    you_will_learn_list = models.TextField(max_length=500000)
    Lessons = models.TextField(max_length=500000)
    category = models.TextField(max_length=500000)
    Requirements = models.TextField(max_length=500000)
    orignal_price = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.TextField(help_text="Enter the duration of the course")
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

class Students(models.Model):
    student_name = models.CharField(max_length=255)
    student_mail = models.CharField(max_length=50) 
    student_phone = models.CharField(max_length=10)

    def __str__(self):
        return self.student_name
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"
    
class Payment(models.Model):
    payment_id = models.CharField(max_length=100, unique=True)
    user_email = models.EmailField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10)
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment {self.payment_id} - {self.status}"