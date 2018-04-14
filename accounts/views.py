from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm

# Create your views here.
def home(request):
    return render(request, 'base.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            base, provider = email.split("@")
            if provider != "lnmiit.ac.in":
                return redirect('/accounts/signup')
            else:
                user = form.save()
                login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form':form})
