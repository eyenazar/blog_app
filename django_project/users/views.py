from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .token import activation_token
from django.shortcuts import get_object_or_404
from django.http import Http404
from users.models import Profile


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.is_active = False
            instance.save()
            site = get_current_site(request)
            mail_subject = "Confirmation message for blog"
            message = render_to_string('users/confirm_email.html', {
                'user': instance,
                'domain': site.domain,
                'uid': instance.id,
                'token': activation_token.make_token(instance)

            })
            to_email = form.cleaned_data.get('email')
            to_list = [to_email]
            from_email = settings.EMAIL_HOST_USER
            send_mail(mail_subject, message, from_email, to_list, fail_silently=True)
            username = form.cleaned_data.get('username')
            return render(request, 'users/confirmation_message.html', {})
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def activate(request, uid, token):
    try:
        user = get_object_or_404(User, pk=uid)
    except:
        raise Http404('No user found')
    if user is not None and activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return render(request, 'users/registration_confirmation_done.html', {})


def profile(request, username):
    custom_user = User.objects.get(username=username)
    return render(request, 'users/profile.html', {'custom_user': custom_user})

@login_required
def profile_edit(request, username):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Profile has been updated!')
            return redirect('profile', username)
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    return render(request, 'users/profile_edit.html', {'u_form': u_form, 'p_form': p_form})
