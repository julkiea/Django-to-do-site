from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

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