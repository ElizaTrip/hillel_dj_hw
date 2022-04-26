from django.shortcuts import render

from .models import EmailForms


def home(request):
    return render(request, 'home.html')


def reset_password(request):
    return render(request, 'reset_password.html', {
        "form": EmailForms(),
    })


def email_verification(request):
    return render(request, 'email_verification.html', {
        "form": EmailForms(),
    })


def welcome_email(request):
    return render(request, 'welcome.email')
