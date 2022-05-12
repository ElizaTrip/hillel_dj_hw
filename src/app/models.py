from django.db import models


class Person(models.Model):
    """
     Model for students and teachers.
    """

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    person_type = models.CharField(max_length=20)
    create_time = models.DateField()
    update_time = models.DateField()
    is_active = models.BooleanField()
    social_url = models.CharField(max_length=80, default='')


class Group(models.Model):
    """
     Model for info about groups
    """

    number = models.IntegerField()
    students_amount = models.IntegerField()


class Subject(models.Model):
    """
     Model for subjects.
    """

    name = models.CharField(max_length=90)
    description = models.CharField(max_length=124)
    hours_in_week = models.IntegerField()


class Course(models.Model):
    """
     Model for course.
    """

    name = models.CharField(max_length=90)
    difficulty = models.IntegerField()


class Lesson(models.Model):
    """
     Модель урока.

     Поля:
      1. Описание урока.
    """

    description = models.CharField(max_length=124)
