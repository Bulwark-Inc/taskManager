from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import CustomUserRegistrationForm
from django.contrib.auth import login
from django.utils import timezone
from datetime import timedelta
from django.db.models import Q
from .forms import TaskForm
from .models import Task


def home(request):
    return render(request, 'tasks/home.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after registration
            return redirect('dashboard')  # Redirect to dashboard after signup
    else:
        form = CustomUserRegistrationForm()

    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserChangeForm(request.POST, instance=request.user)
        password_form = PasswordChangeForm(request.user, request.POST)

        if user_form.is_valid() and password_form.is_valid():
            user_form.save()
            password_form.save()
            update_session_auth_hash(request, password_form.user)  # Important!
            return redirect('profile')
    else:
        user_form = UserChangeForm(instance=request.user)
        password_form = PasswordChangeForm(request.user)

    return render(request, 'users/profile.html', {
        'user_form': user_form,
        'password_form': password_form
    })

# Dashboard (List tasks)
@login_required
def dashboard(request):
    filter_option = request.GET.get('filter', 'all')
    query = request.GET.get('q', '')

    tasks = Task.objects.filter(user=request.user)

    if filter_option == 'completed':
        tasks = tasks.filter(completed=True)
    elif filter_option == 'active':
        tasks = tasks.filter(completed=False)

    if query:
        tasks = tasks.filter(Q(title__icontains=query) | Q(description__icontains=query))
    
    now = timezone.now()
    upcoming_tasks = Task.objects.filter(user=request.user, due_date__gte=now, due_date__lte=now + timedelta(days=1), completed=False)

    return render(request, 'tasks/dashboard.html', {
        'tasks': tasks,
        'upcoming_tasks': upcoming_tasks,
    })

# Create task
@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('dashboard')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form, 'title': 'Add Task'})

# Edit task
@login_required
def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form, 'title': 'Edit Task'})

# Delete task
@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('dashboard')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})
