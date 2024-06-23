from django.shortcuts import render, redirect
from .models import Book
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def home(request, name=None):
    books = Book.objects.all()
    if name is None:
        name = request.GET.get('name', 'Guest') 

    context = {
        'user_name': name, 'books':books
    }
    return render(request, 'home.html', context)



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password is incorrect.')
    
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('home')

def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            messages.success(request, 'You have been successfully registered.')
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration.')

    return render(request, 'register.html', {'form': form})