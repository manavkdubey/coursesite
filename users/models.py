from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    date_registered = models.DateTimeField(auto_now_add=True)
    enrolled_courses = models.ManyToManyField(
        'courses.Course',
        blank=True
    )