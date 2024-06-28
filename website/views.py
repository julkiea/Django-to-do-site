from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm

def home(request):
    
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
            return redirect('home')
    
    # If not logging in
    else:

        # Render home page
        return render(request, 'home.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out successfully!")
    return redirect('home')

def register_user(request):

    # Check if signing in
    if request.method == 'POST':

        # Create instance of SignUpForm
        form = SignUpForm(request.POST)

        # Check if form is valid
        if form.is_valid():

            # Save new user in data base
            form.save

            # Get username and password from cleaned data from form
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            # Authenticate user
            user = authenticate(username=username, password=password)

            # If authenticating is success
            messages.success(request, "You have been signed in successfully")

            # Redirect home
            return redirect('home')
        
        else:
            form = SignUpForm()
            return render(request, 'register.html', {'form': form})
        
    return render(request, 'register.html', {'form': form})