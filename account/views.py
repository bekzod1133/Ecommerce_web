from django.contrib.auth import login, authenticate
from django.shortcuts import render,redirect
from .forms import CreateUserF

def RegistrationView(request):
    form = CreateUserF()

    if request.method == "POST":
        form = CreateUserF(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form': form}
    return render(request, 'account/register.html', context)

def LoginView(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

    context = {}
    return render(request, 'account/login.html', context)

from django.contrib.auth import logout


def logout_view(request):
    logout(request)
    return redirect('home')


