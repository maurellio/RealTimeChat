from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm

# Create your views here.
def fronpage(request):
    return render(request, 'core/frontpage.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        print(form.errors)
        if form.is_valid():

            user = form.save()

            login(request, user)
            return redirect('frontpage')

    else:
        form = SignUpForm()

    return render(request, 'core/signup.html', {'form' : form})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('frontpage')
        else:
            return render(request, 'core/login.html', {'error': 1})
    else:
        return render(request, 'core/login.html', {'error': 0})