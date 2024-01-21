from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .models import Course
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponseBadRequest
from django.contrib import messages

def home(request):
    courses = Course.objects.all()  # Retrieves all Course objects from the database
    return render(request, 'registration/home.html', {'courses': courses})

@login_required
def buy_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    
    if request.user in course.enrolled_users.all():
        messages.error(request, 'You are already enrolled in this course')
        return redirect('account')  # Redirect to a relevant page

    # Simulate payment processing and enroll the user
    course.enrolled_users.add(request.user)
    course.save()

    messages.success(request, 'You have successfully enrolled in the course!')
    return redirect('account')  # Redirect to a relevant page

from .forms import AddCourseForm  # Import the AddCourseForm

def add_course(request):
    if request.method == 'POST':
        form = AddCourseForm(request.POST, request.FILES)
        if form.is_valid():
            course = form.save()
            return redirect('home')  # Redirect to the courses page after course creation
    else:
        form = AddCourseForm()
    return render(request, 'registration/add_course_form.html', {'form': form})
