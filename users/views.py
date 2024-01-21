from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import CustomUserCreationForm



@login_required
def account(request):
    # Your logic to fetch the user's enrolled courses might look like this:
    enrolled_courses = request.user.courses_enrolled.all()
    return render(request, 'registration/account.html', {'enrolled_courses': enrolled_courses})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('account')  # This should match the name of your account URL pattern
        else:
            print(form.errors)  # Log any form errors
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
# Create your views here.
