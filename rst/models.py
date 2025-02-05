from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name

class Exam_Officer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=False)
    email = models.EmailField(null=False)

    def __str__(self):
        return self.user.first_name

class Course(models.Model):
    code = models.CharField(max_length=7, null=False)
    title = models.CharField(max_length=100, null=False)
    unit_load = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.code

class Parent(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, null=True)
    phone_no = models.CharField(max_length=13, null=False)
    email = models.EmailField(null=False)

    def __str__(self):
        return self.user.username

class Student(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    reg_no= models.CharField("Registration Number", max_length=11)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    email = models.EmailField(null=False)
    parent = models.ForeignKey(Parent, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.reg_no


class Grade(models.Model):
    grade = models.CharField(max_length=1)
    

    def __str__(self):
        return self.grade

class Semester(models.Model):
    semester = models.CharField(max_length=11)
    def __str__(self):
        return self.semester

class Session(models.Model):
    session = models.CharField(max_length=9)
    def __str__(self):
        return self.session

class Level(models.Model):
    level = models.CharField(max_length=3)
    def __str__(self):
        return self.level

class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    grade = models.ForeignKey(Grade, on_delete=models.SET_NULL, null=True)
    semester = models.ForeignKey(Semester, on_delete= models.SET_NULL, null=True)
    session = models.ForeignKey(Session, on_delete= models.SET_NULL, null=True)
    level = models.ForeignKey(Level, on_delete= models.SET_NULL, null=True)
    exam_score = models.IntegerField(null=True)
    ca_score = models.IntegerField(null=True)

    def __str__(self):
        return self.student.reg_no if self.student else "unassigned result"


class Head_Of_Department(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.user.first_name

class School_Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    designation = models.CharField(max_length=30)

    def __str__(self):
        return self.user.first_name