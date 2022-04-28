from django.shortcuts import render

from .email import send
from .models import EmailForms


def home(request):
    return render(request, 'home.html')


def email_send(request):
    send(
        "Reset password",
        "eliza.tripolskaya21@gmail.com",
        "reset_password",
    )
    return render(request, 'email_send.html')


def reset_password(request):
    return render(request, 'reset_password.html')


def email_verification(request):
    return render(request, 'email_verification.html', {
        "form": EmailForms(),
    })


def welcome_email(request):
    return render(request, 'welcome.email')
