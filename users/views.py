from .forms import CustomUserCreationForm, CustomUserChangeForm

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.utils.http import url_has_allowed_host_and_scheme
from django.utils.translation import gettext as _
from django.conf import settings


# Create your views here.
def loginPage(request):
    if request.user.is_authenticated:
        return redirect(settings.HOME_PAGE_URL_NAME)

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        next_ = request.GET.get('next', settings.HOME_PAGE_URL_NAME)
        if not url_has_allowed_host_and_scheme(next_, allowed_hosts=settings.ALLOWED_HOSTS):
            next_ = settings.HOME_PAGE_URL_NAME
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, _("Bienvenue  ") + user.get_username())
            return redirect(next_)
        else:
            messages.warning(request, _("Nom d'utilisateur ou mot de passe est incorrect")) # noqa

    return render(request, "users/login_page.html", {})


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, _("Bonjour  ")+user.username+_(", votre compte a été crée avec succès"))  # noqa
            return redirect(settings.HOME_PAGE_URL_NAME)
    else:
        form = CustomUserCreationForm()
    context = {'title': 'Login', 'form': form}
    return render(request, 'users/signup.html', context)


def updateUser(request):
    if request.method == "POST":
        form = CustomUserChangeForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, _("Votre compte a été modifié avec succès"))  # noqa
            return redirect(settings.HOME_PAGE_URL_NAME)
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {'title': 'Profile', 'form': form}
    return render(request, 'users/signup.html', context)


def logoutUser(request):
    logout(request)
    return redirect(settings.LOGIN_URL_NAME)
