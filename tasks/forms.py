from django import forms
from .models import Task
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import PasswordChangeForm

# Task Creation form
class TaskForm(forms.ModelForm):
    due_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'completed']
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded focus:outline-none focus:ring focus:border-blue-300'}),
            'description': forms.Textarea(attrs={'class': 'w-full px-4 py-2 border rounded focus:outline-none focus:ring focus:border-blue-300'}),
            'completed': forms.CheckboxInput(attrs={'class': 'h-4 w-4 text-blue-600 focus:ring focus:ring-blue-300'}),
        }

# Custom User Registration form
class CustomUserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={'class': 'appearance-none rounded w-full py-2 px-3 border border-gray-300 placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500'}
    ))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'class': 'appearance-none rounded w-full py-2 px-3 border border-gray-300 placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'appearance-none rounded w-full py-2 px-3 border border-gray-300 placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'appearance-none rounded w-full py-2 px-3 border border-gray-300 placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500'
        })

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

# Custom login form
class CustomLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'class': 'appearance-none rounded w-full py-2 px-3 border border-gray-300 placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500'
        })

        self.fields['password'].widget.attrs.update({
            'class': 'appearance-none rounded w-full py-2 px-3 border border-gray-300 placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500'
        })


# Custom User update form
class UserUpdateForm(forms.ModelForm):
    """Form to update username and email."""

    class Meta:
        model = User
        fields = ['username', 'email']

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        # Optional: customize form fields (add placeholders, CSS classes, etc.)
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Enter your username',
        })
        self.fields['email'].widget.attrs.update({
            'placeholder': 'Enter your email',
        })


# Custom Password Update form
class CustomPasswordChangeForm(PasswordChangeForm):
    """Optional: Extend the built-in PasswordChangeForm to add custom behavior."""

    def __init__(self, *args, **kwargs):
        super(CustomPasswordChangeForm, self).__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs.update({
            'placeholder': 'Enter old password',
        })
        self.fields['new_password1'].widget.attrs.update({
            'placeholder': 'Enter new password',
        })
        self.fields['new_password2'].widget.attrs.update({
            'placeholder': 'Confirm new password',
        })