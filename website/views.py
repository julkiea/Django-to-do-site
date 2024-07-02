from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddATaskForm
from .models import Task


def activate_email(request, user, to_email):
    messages.success(request, f'Dear {user}, please go to your email: {to_email}, inbox and click \
                     on received activation link to confirm and complete the registration. Note: Check your spam folder.')

@login_required
def home(request):
    
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'home.html', {'tasks': tasks})

def login_user(request):
    # Check if logging in
    if request.method == "POST":
        
        # Get username and password:
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate user
        user = authenticate(request, username = username, password = password)

        # If authenticating is success
        if user is not None:

            # Log in 
            login(request, user)
             
            # Display message 
            messages.success(request, 'You have been logged in successfully!')

            # Redirect home
            return redirect('home')
        
        # If authenticating is not success
        else:
            messages.success(request, 'An error occurred while logging in, please try again!')
            
            # Redirect home
            return redirect('login.html')
    
    # If not logging in
    else:

        # Render home page
        return render(request, 'login.html')


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out successfully!")
    return redirect('login')

def register_user(request):

    # Check if signing in
    if request.method == 'POST':

        # Create instance of SignUpForm
        form = SignUpForm(request.POST)

        # Check if form is valid
        if form.is_valid():

            # Create a user 
            form.save()
            """user.is_active = False

            # Save a user
            user.save()
            
            activate_email(request, user, form.cleaned_data.get('email'))
            # Redirect home
            return redirect('home')"""

            
            # Get username and password from cleaned data from form
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            # Authenticate user
            user = authenticate(username=username, password=password)
            
            if user is not None:

                login(request, user)

                # If authentication is successful
                messages.success(request, "You have been signed up successfully")

                # Redirect home
                return redirect('home')
            
            else:
                messages.success(request, "Authentication failed. Please try again.")
 
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})

    return render(request, 'register.html', {'form': form})


def add_task(request):

    # Check if logged in 
    if request.user.is_authenticated:

        # Check if filling the form
        if request.method == 'POST':
            form = AddATaskForm(request.POST)

            # Check if form is valid
            if form.is_valid():

                task = form.save(commit=False)

                # Set the user to the currently logged in user
                task.user = request.user  

                # Save the task
                task.save()
                messages.success(request, "To-do task has been added successfully!")
                
                # Redirect home
                return redirect('home')
            
        # If not filling the form
        else:
            form = AddATaskForm()
        return render(request, 'add_task.html', {'form': form})
    
    # If user is not logged in
    else:
        messages.success(request, "You must be logged in. Log in and try again...")
        return redirect('home')

def task(request, pk):
    # Check if logged in 
    if request.user.is_authenticated:
        try:
            task = get_object_or_404(Task, id=pk, user=request.user)
            return render(request, 'task.html', {'task': task})
        except Task.DoesNotExist:
            messages.error(request, "Task does not exist.")
            return redirect('home')
    
    # If not logged in 
    else: 
        messages.success(request, "You must be logged in! Log in and try again...")
        return redirect('home')
    
def delete_task(request, pk):
    if request.user.is_authenticated:
        try:
            task_to_delete = get_object_or_404(Task, id=pk, user=request.user)
            task_to_delete.delete()
            messages.success(request, "Task has been deleted successfully")
        except Task.DoesNotExist:
            messages.error(request, "Task does not exist.")
        return redirect('home')
        
    else:
        messages.success(request, "You must be logged in! Log in and try again...")
        return redirect('home')
