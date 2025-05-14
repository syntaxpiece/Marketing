from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Information(models.Model):
    LOCATION_CHOICES = [
        ('pal', 'Palestine'),
        ('egy', 'Egypt'),
        ('sud', 'Saudi Arabia'),
        ('jor', 'Jordan'),
    ]

    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=10, choices=LOCATION_CHOICES)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    img = models.ImageField(null=True, blank=True, upload_to='img/users')
    video = models.FileField(upload_to='video', null=True,blank=True)
    birthday = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class SocialIcon(models.Model):
    name = models.CharField(max_length=50)
    link = models.URLField()
    def __str__(self):
        return self.name
    

class Links (models.Model):
    name = models.CharField(max_length=50)
    link = models.URLField()
    img = models.ImageField(upload_to='img/links')

    def __str__(self):
        return self.name


class Product (models.Model):
    name = models.CharField(max_length=50)
    link = models.URLField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    img = models.ImageField(upload_to='img/products')

    def __str__(self):
        return self.name

class Course (models.Model):
    name = models.CharField(max_length=50)
    link = models.URLField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    img = models.ImageField(upload_to='img/courses')

    def __str__(self):
        return self.name

class Consultation (models.Model):
    name = models.CharField(max_length=50)
    link = models.URLField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    img = models.ImageField(upload_to='img/consultations')

    def __str__(self):
        return self.name

