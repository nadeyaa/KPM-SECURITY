from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm
from .models import Profile

def is_admin(user):
    return user.role == 'admin'

def is_guard(user):
    return user.role == 'guard'

@login_required
@user_passes_test(is_admin)
def admin_view(request):
    # Your admin view logic here
    return render(request, 'admin_template.html')

@login_required
@user_passes_test(is_guard)
def guard_view(request):
    # Your security guard view logic here
    return render(request, 'guard_template.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            role = form.cleaned_data.get('role')
            Profile.objects.create(user=user, role=role)
            login(request, user)
            if role == 'admin':
                return redirect('admin:index')  # Redirect to the admin index page
            else:
                return redirect('security_guard:index')  # Redirect to the security guard page
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})