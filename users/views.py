from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your acount have been created successfully. You can login now!')
            return redirect('login')
        else:
            messages.warning(request, f'Information entered is not vaalid!\nCheck details and try again.')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
