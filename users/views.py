from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile
from django.db import IntegrityError

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            try:
                # Check if the profile already exists
                if not Profile.objects.filter(user=user).exists():
                    Profile.objects.create(user=user)
                username = form.cleaned_data.get('username')
                messages.success(request, f'Account created for {username}!')
                return redirect('login')
            except IntegrityError:
                # Handle the case where the profile creation fails due to uniqueness constraint
                messages.error(request, 'Profile for this user already exists.')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})





from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserUpdateForm, ProfileUpdateForm
from .models import Profile

@login_required
def profile(request):
    user = request.user
    # Ensure the profile exists for the user
    profile, created = Profile.objects.get_or_create(user=user)

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=user)
        p_form = ProfileUpdateForm(instance=profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)



