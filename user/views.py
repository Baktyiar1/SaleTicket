from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

from .forms import RegisterUserForm


def register_views(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Регистрация успешно')
            return redirect('index')

        for key, error in form.errors.items():
            for err in error:
                messages.error(request, f'{err}')

    return redirect('index')


def login_views(request):
    if request.method == 'POST':
        phone_number = request.POST['phone_number']
        password = request.POST['password']

        user = authenticate(request, phone_number=phone_number, password=password)

        if user:
            login(request, user)
            messages.success(request,'Вы успешено вошли в систему.')

            return redirect('index')
        messages.error(request,'Неверный логин или пароль.')

        return redirect('index')


def logout_views(request):
    logout(request)
    messages.success(request, 'Вы успешено вышли из системы.')
    return redirect('index')