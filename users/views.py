from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserChangeForm,UserForm,UserTypeCreationForm,UserTypeCreationAddressForm
from .models import User, UserType


def create_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST,request.FILES)
        print('hamdy adam ')
        print(request.POST)
        if form.is_valid():
            print('form is valid')
            user = form.save()
            # Do something with the new user object\
            return redirect('/users/create')
        print(form.errors)

    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


def update_user(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            # Do something with the updated user object
            return redirect('home')
    else:
        form = CustomUserChangeForm(instance=user)
    return render(request, 'update_user.html', {'form': form})


def user_detail(request, user_id):
    user = User.objects.get(id=user_id)
    form = UserForm(instance=user)
    return render(request, 'user_detail.html', {'user': user, 'form': form})


def create_user_type(request):
    if request.method == 'POST':
        form = UserTypeCreationForm(request.POST,request.FILES)
        print('hamdy adam ')
        print(request.POST)
        if form.is_valid():
            print('form is valid')
            user_type = form.save()
            print(user_type,'dsssssssssssssssssss')
            print(user_type.slug)
            return redirect(f"/users/create_address_user_type/{user_type.slug}")
        print(form.errors)

    else:
        form = UserTypeCreationForm()
    return render(request, 'add_user_type.html', {'form': form})


def create_user_type_address(request, slug):
    if request.method == 'POST':
        form = UserTypeCreationAddressForm(request.POST)
        print('hamdy adam ')
        print(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user_type = UserType.objects.filter(slug=slug).first()
            address.save()
            return redirect('/users/create')
        print(form.errors)

    else:
        form = UserTypeCreationAddressForm()
    return render(request, 'add_address.html', {'form': form})