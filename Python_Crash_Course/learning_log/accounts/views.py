from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """Register a new user"""
    if request.method != 'POST':
        ## Display blank registration form
        form = UserCreationForm()
    else:
        ## Process completed form
        form = UserCreationForm(data=request.POST)  ## Create an instance of UserCreationForm with submitted data
        
        if form.is_valid():             ## If username and password is correct. Also user is not trying to do anything malicious in their submission.
            new_user = form.save()      ## If data valid, save the username and hash of password to the database. Save() method returns new obj 'new_user'
            ## Log the user in and then redirect to home page
            login(request, new_user)    ## call the login function with request and new_user obj which creates a valid session.
            return redirect('learning_logs:index')  ## Finally we redirect user to home page.
        
    ## Display a blank or invalid form.
    context = {'form':form}
    return render(request, 'registration/register.html', context)
