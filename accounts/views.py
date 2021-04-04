from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def signup(request):
    if request.user.is_authenticated:
        return redirect('recipes:home')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('accounts:login')
        else:
            return render(request, 'registration/signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'registration/signup.html', {'form': form})


def signin(request):
    if request.user.is_authenticated:
        return render(request, 'recipes:home')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('recipes:home')
        else:
            form = AuthenticationForm(request.POST)
            return render(request, 'registration/signin.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'registration/signin.html', {'form': form})

def signout(request):
    if not request.user.is_authenticated:
        form = AuthenticationForm()
        return redirect(reverse('accounts:login'))
    else:
        logout(request)
        form = AuthenticationForm()
        return redirect(reverse('accounts:login'))
    