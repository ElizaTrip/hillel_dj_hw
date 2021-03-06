"""hillel_dj_hw URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from app.views import home, email_send, sign_in, logging_out, register, activate
from app.views import SubjectSelect, SubjectUpdate
from app.views import TeacherSelect, TeacherUpdate
from app.views import StudentSelect, StudentDetail
from app.views import PersonViewSet, GroupViewSet, SubjectViewSet


router = routers.DefaultRouter()
router.register(r'person', PersonViewSet)
router.register(r'group', GroupViewSet)
router.register(r'subject', SubjectViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('email_send', email_send),

    path('api/', include(router.urls)),


    path('subjects', SubjectSelect.as_view(), name="subjects_list"),
    path('sub_update/<int:pk>', SubjectUpdate.as_view(), name='subjects_update'),

    path('teachers', TeacherSelect.as_view(), name="teachers_list"),
    path('teacher_update/<int:pk>', TeacherUpdate.as_view(), name='teachers_update'),

    path('students', StudentSelect.as_view(), name="student_list"),
    path('student_detail/<int:pk>', StudentDetail.as_view(), name="student_detail"),

    path('login', sign_in, name='login'),
    path('logout', logging_out, name='logout'),

    path('signup', register, name='signup'),
    path('verify_account/<str:uid>/<str:token>', activate, name='verify_account'),
]
