from django.db import models


class Person(models.Model):
    """
     Модель Person.

     Поля:
      1. Имя.
      2. Фамилия.
      3. Возраст.
      4. Тип (учитель/студент).
      5. Дата создания.
      6. Дата посл. обовления.
      7. Активен ли аккаунт.
    """

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    person_type = models.CharField(max_length=20)
    create_time = models.DateField()
    update_time = models.DateField()
    is_active = models.BooleanField()


class Group(models.Model):
    """
     Модель группы.

     Поля:
      1. Номер.
      2. Кол-во учащихся.
    """

    group_num = models.IntegerField()
    stud_in_group = models.IntegerField()


class Subject(models.Model):
    """
     Модель предмета.

     Поля:
      1. Название.
      2. Описание.
      3. Количество часов в неделю.
    """

    sub_name = models.CharField(max_length=90)
    sub_desc = models.CharField(max_length=124)
    hours_in_week = models.IntegerField()


class Course(models.Model):
    """
     Модель курса.

     Поля:
      1. Наименование.
      2. Сложность.
    """

    course_name = models.CharField(max_length=90)
    difficulty = models.IntegerField()


class Lesson(models.Model):
    """
     Модель урока.

     Поля:
      1. Описание урока.
    """

    lesson_desc = models.CharField(max_length=124)
