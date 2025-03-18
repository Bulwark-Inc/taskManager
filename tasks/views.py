from datetime import timedelta

from django.contrib import messages
from django.contrib.auth import login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils import timezone

from .forms import (
    CustomUserRegistrationForm,
    TaskForm,
    UserUpdateForm,
    CustomPasswordChangeForm
)
from .models import Task


def home_view(request):
    """Render the homepage."""
    return render(request, 'tasks/home.html')


def register_view(request):
    """Handle user registration."""
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after registration
            messages.success(request, 'Registration successful. Welcome!')
            return redirect(reverse('dashboard'))
    else:
        form = CustomUserRegistrationForm()

    return render(request, 'registration/register.html', {'form': form})


@login_required
def profile_view(request):
    """View and update user profile and password."""
    if request.method == 'POST':
        form_type = request.POST.get('form_type')

        if form_type == 'profile':
            user_form = UserUpdateForm(request.POST, instance=request.user)
            password_form = CustomPasswordChangeForm(user=request.user)  # Empty password form

            if user_form.is_valid():
                user_form.save()
                messages.success(request, 'Profile updated successfully.')
                return redirect(reverse('profile'))

        elif form_type == 'password':
            password_form = CustomPasswordChangeForm(user=request.user, data=request.POST)
            user_form = UserUpdateForm(instance=request.user)  # Empty user form

            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)  # Prevent logout after password change
                messages.success(request, 'Password changed successfully.')
                return redirect(reverse('profile'))

        else:
            # Fallback for unexpected form_type
            user_form = UserUpdateForm(instance=request.user)
            password_form = CustomPasswordChangeForm(user=request.user)

    else:
        user_form = UserUpdateForm(instance=request.user)
        password_form = CustomPasswordChangeForm(user=request.user)

    return render(request, 'users/profile.html', {
        'user_form': user_form,
        'password_form': password_form
    })


@login_required
def dashboard_view(request):
    """Display user dashboard with tasks."""
    filter_option = request.GET.get('filter', 'all')
    query = request.GET.get('q', '')

    now = timezone.now()

    # Get base queryset for the user
    user_tasks = Task.objects.filter(user=request.user)

    # Filter tasks
    if filter_option == 'completed':
        tasks = user_tasks.filter(completed=True)
    elif filter_option == 'active':
        tasks = user_tasks.filter(completed=False)
    else:
        tasks = user_tasks

    # Search query
    if query:
        tasks = tasks.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        )

    # Upcoming tasks within the next day
    upcoming_tasks = user_tasks.filter(
        due_date__gte=now,
        due_date__lte=now + timedelta(days=1),
        completed=False
    )

    return render(request, 'tasks/dashboard.html', {
        'tasks': tasks,
        'upcoming_tasks': upcoming_tasks,
    })


@login_required
def task_create_view(request):
    """Create a new task."""
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, 'Task created successfully!')
            return redirect(reverse('dashboard'))
    else:
        form = TaskForm()

    return render(request, 'tasks/task_form.html', {
        'form': form,
        'title': 'Add Task'
    })


@login_required
def task_edit_view(request, pk):
    """Edit an existing task."""
    task = get_object_or_404(Task, pk=pk, user=request.user)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated successfully!')
            return redirect(reverse('dashboard'))
    else:
        form = TaskForm(instance=task)

    return render(request, 'tasks/task_form.html', {
        'form': form,
        'title': 'Edit Task'
    })


@login_required
def task_delete_view(request, pk):
    """Delete a task after confirmation."""
    task = get_object_or_404(Task, pk=pk, user=request.user)

    if request.method != 'POST':
        return render(request, 'tasks/task_confirm_delete.html', {'task': task})

    task.delete()
    messages.success(request, 'Task deleted successfully!')
    return redirect(reverse('dashboard'))
