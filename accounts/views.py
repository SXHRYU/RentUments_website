from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

# Create your views here.
def login_view(request, *args, **kwargs):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username,
            password=password)
        if user is None:
            context = {'error': 'Invalid username or password.'}
            return render(request, 'login.html', context)
        login(request, user)
        return redirect('/home')
    return render(request, 'login.html', {})