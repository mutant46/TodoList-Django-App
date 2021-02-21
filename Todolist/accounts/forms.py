from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=99,
    help_text="No special char",
    label=('First Name'),
    )

    password1 = forms.CharField(label=("Password"),
    widget=forms.PasswordInput,
    help_text="min. 8 char",
    )

    password2 = forms.CharField(label=("Confirm Password"),
    widget=forms.PasswordInput,
    help_text="Same as above",
    )

    username = forms.CharField(label=("Username"),
    help_text="only letters, numbers and underscores",
    )

    email = forms.EmailField(label=("Email"),
    help_text="only letters, numbers and underscores",
    )

    class Meta:
        model = User
        fields = ('first_name', 'username', 'email' ,'password1', 'password2',)

    