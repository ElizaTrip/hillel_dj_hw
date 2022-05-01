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


