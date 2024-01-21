from django import forms
from .models import Course  # Import the Course model

class AddCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'image']
