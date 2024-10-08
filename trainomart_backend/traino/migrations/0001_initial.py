# Generated by Django 5.1.1 on 2024-10-04 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=255)),
                ('blog_image', models.ImageField(upload_to='blogs/')),
                ('blog_data', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=255)),
                ('course_image', models.ImageField(upload_to='courses/')),
                ('description', models.TextField(max_length=500000)),
                ('course_content', models.TextField(max_length=500000)),
                ('you_will_learn_list', models.TextField(max_length=500000)),
                ('Lessons', models.TextField(max_length=500000)),
                ('category', models.TextField(max_length=500000)),
                ('Requirements', models.TextField(max_length=500000)),
                ('orignal_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('duration', models.TextField(help_text='Enter the duration of the course')),
                ('language', models.CharField(max_length=100)),
                ('skill_level', models.CharField(choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced')], max_length=50)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('is_featured', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Leads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('payment_status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=255)),
                ('student_mail', models.CharField(max_length=50)),
                ('student_phone', models.CharField(max_length=10)),
            ],
        ),
    ]
