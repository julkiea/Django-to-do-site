from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Task


# Creating SignUpForm class
class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email address: '}))
    first_name = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First name: '}))
    last_name = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last name: '}))

    class Meta():
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'



# Creating AddATaskForm
class AddATaskForm(forms.ModelForm):
    PRIORITY_CHOICES = [
        ('L', 'Low'),
        ('M', 'Medium'),
        ('H', 'High'),
    ]
    title = forms.CharField(label="Title", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter task title'}))
    description = forms.CharField(label="Description", widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter task description'}))
    category = forms.CharField(label="Category", required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter task category'}))
    deadline = forms.DateTimeField(label="Deadline", required=False, widget=forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Select deadline', 'type': 'datetime-local'}))
    priority = forms.ChoiceField(label="Priority", choices=PRIORITY_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    completed = forms.BooleanField(label="Completed", required=False)

    class Meta():
        model = Task
        fields = ('title', 'description', 'category', 'deadline', 'priority', 'completed')
