from django.db import models
from django.conf import settings
class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='courses/images/')
    created_date = models.DateTimeField(auto_now_add=True)
    enrolled_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='courses_enrolled',  # Make sure this related_name is unique
        blank=True
    )
