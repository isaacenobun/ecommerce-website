from django.shortcuts import redirect, render
from .forms import UserRegisterForm
from django.contrib.auth import login, authenticate
from django.contrib import messages

# Create your views here.
def account(request):
    form =  UserRegisterForm()
    if request.method == 'POST':
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
            return redirect('home')
    else:
        form = UserRegisterForm()
    context = {'form':form,'title': 'Account - Redstore', 'header':'header2'}
    return render(request, 'userauths/account.html', context)