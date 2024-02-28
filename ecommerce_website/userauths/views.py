from django.shortcuts import redirect, render
from .forms import UserRegisterForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.conf import settings

from django.apps import apps
User = apps.get_model(*settings.AUTH_USER_MODEL.split('.'))

# Create your views here.
def account(request):
    logged_in = request.user.is_authenticated
    if logged_in:
        return redirect('home')

    form =  UserRegisterForm()

    if request.method == 'POST':
        if 'register' in request.POST:
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                new_user = form.save()
                username = form.cleaned_data.get('username')
                messages.success = (request, f'Hey {username}, your account was created succesfully')
                new_user = authenticate(
                    username=form.cleaned_data['username'],
                    password = form.cleaned_data['password1']
                )
                login(request, new_user)
                return redirect('home',{'logged_in':logged_in})
            
        elif 'login' in request.POST:
            email = request.POST.get('email')
            password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.warning(request, f"User with {email} does not exist")
            return redirect('account')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You are logged in")
            return redirect('home')
        else:
            messages.warning(request, "Invalid email or password")
            return redirect('account')

    
    else:
        form = UserRegisterForm()
        
    context = {'form':form,'title': 'Account - Redstore', 'header':'header2'}
    return render(request, 'userauths/account.html', context)

def log_out(request):
    logout(request)
    messages.warning(request, "You logged out.")
    return redirect('account')