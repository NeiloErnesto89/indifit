from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


#form inherits from user creation

class UserRegisterForm(UserCreationForm):  # class inherits from UserCreationForm
    email = forms.EmailField()  # additional fields (required=True by default)

    class Meta:
        model = User  # specifies model our form interacts with as when form is valid, it creates new user
        fields = ['username', 'email', 'password1', 'password2']  # fields are shown on form (in order)

            # class Meta gives nested namespace for conifgs and keeps them in one place
            # we are saying in the Meta that user model is affected - form.save() is saved to user model