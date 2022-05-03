from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from .email import send
from .models import Subject, Person


def home(request):
    return render(request, 'home.html')


class SubjectSelect(ListView):
    model = Subject
    template_name = "subject_list.html"


class SubjectUpdate(UpdateView):
    model = Subject
    fields = ["sub_name", "sub_desc", "hours_in_week"]
    template_name = "sub_update.html"
    success_url = reverse_lazy("subjects_list")


class TeacherSelect(ListView):
    model = Subject
    template_name = "teacher_list.html"


class PersonCreate(CreateView):
    model = Person
    fields = ["first_name", "last_name", "age", "person_type", "create_time",
              "update_time", "is_active"]
    template_name = "student_create.html"
    success_url = reverse_lazy("subjects_list")


def email_send(request):
    send(
        "Reset password",
        "eliza.tripolskaya21@gmail.com",
        "reset_password",
    )
    return render(request, 'email_send.html')
