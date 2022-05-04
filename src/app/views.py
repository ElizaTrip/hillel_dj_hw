from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView

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
    model = Person
    template_name = "teacher_list.html"


class TeacherUpdate(UpdateView):
    model = Person
    fields = ["first_name", "last_name", "age", "person_type",
              "update_time", "is_active"]
    template_name = "teacher_update.html"
    success_url = reverse_lazy("teachers_list")


class StudentSelect(ListView):
    model = Person
    template_name = "student_list.html"


class StudentDetail(DetailView):
    model = Person
    template_name = 'student_detail.html'


def email_send(request):
    send(
        "Reset password",
        "eliza.tripolskaya21@gmail.com",
        "reset_password",
    )
    return render(request, 'email_send.html')
