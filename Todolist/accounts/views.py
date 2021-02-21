from django.shortcuts import render ,redirect
from .forms import SignUpForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import login
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
# Create your views here.


def createaccount(request):
    if request.method == 'POST':
        form =  SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = SignUpForm()
    return render(request, 'html/signup.html', {'form' : form})




def profile(request):
    return render(request, 'html/profile.html')
