from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.

def register(request):
    # create a form passed to template

    if request.method == "POST":  # checking for equality
        form = UserRegisterForm(request.POST)  # if true, we create/instantiate a user creation form with POST request data i.e. new user
        if form.is_valid():
            form.save()  #saves user and hashes pw - run save method
            username = form.cleaned_data.get('username')  # validated form data in cleaned_data dict in python type
            # flashed message one time display
            # messages.debug # .info  # .success # .error # .warning
            messages.success(request, f'Account created for {username}!')
            return redirect('fitness-programs')  #name of url pattern

    else:
        form = UserRegisterForm()  # create//instantiate a new (blank) instance - anything that's not post reuqests

    return render(request, 'users/register.html', {'form': form} )  # render a template that uses this form, first arg is request
    # { 'form': form } = key is new variable we access on template and value is new instance of UserCreationform

