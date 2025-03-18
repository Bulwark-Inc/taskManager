from . import views
from django.urls import path
from .forms import CustomLoginForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('register/', views.register_view, name='register'),
    
    # Login / Logout route
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='registration/login.html',
            authentication_form=CustomLoginForm
        ),
        name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    # Password reset route
    path('password-reset/', 
        auth_views.PasswordResetView.as_view(
            template_name='registration/password_reset.html',
            email_template_name='registration/password_reset_email.txt',  # HTML email
            subject_template_name='registration/password_reset_subject.txt',
            success_url='done/'
        ), 
        name='password_reset'),
         
    path('password-reset/done/', 
         auth_views.PasswordResetDoneView.as_view(
             template_name='registration/password_reset_done.html'
         ), 
         name='password_reset_done'),
         
    path('reset/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(
             template_name='registration/password_reset_confirm.html'
         ), 
         name='password_reset_confirm'),
         
    path('reset/done/', 
         auth_views.PasswordResetCompleteView.as_view(
             template_name='registration/password_reset_complete.html'
         ), 
         name='password_reset_complete'),

    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('tasks/add/', views.task_create_view, name='task_create'),
    path('tasks/<int:pk>/edit/', views.task_edit_view, name='task_edit'),
    path('tasks/<int:pk>/delete/', views.task_delete_view, name='task_delete'),
    path('profile/', views.profile_view, name='profile'),
]


urlpatterns += [
    
]
