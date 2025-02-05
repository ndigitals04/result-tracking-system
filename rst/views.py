from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import RegisterUserForm
from django.contrib import messages
from django.urls import reverse
from django.core.mail import send_mail
from .models import Student, Parent, Department, Course, Grade, Semester, Session,Level, Result
from django.contrib.auth.models import User
from .send_email import send_email_to_registered_users, send_email_for_newly_published_result
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.
@login_required(login_url= "rst:login")
def index(request):
    if request.user.is_staff:
        return HttpResponseRedirect(reverse("rst:adminPage"))
    context= {
        "user": request.user.first_name,
    }
    return render(request, "rst/index.html", context)

@staff_member_required
def adminDashboard(request):
    context= {
        "user":request.user.first_name
    }
    return render (request, "rst/adminpage.html", context)

def login_view(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return HttpResponseRedirect(reverse("rst:adminPage"))
        return HttpResponseRedirect(reverse("rst:index"))
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if request.user.is_staff:
                return HttpResponseRedirect(reverse("rst:adminPage"))
            return HttpResponseRedirect(reverse("rst:index"))
    context = {}
    return render(request, "rst/login.html", context)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("rst:login"))

def signup(request):
    form = RegisterUserForm()
    departments = Department.objects.all()
    context = {'form': form,
                'departments':departments
    }
    
    if request.method == "POST":
        print("Post data received")
        form = RegisterUserForm(request.POST)
        parent_email = request.POST.get("parent-email")
        if not parent_email:
            form = RegisterUserForm()
            context = {
                "form": form,
                "error":"Parent email must be present",
                "departments":departments
            }
            return render(request, "rst/signup.html", context)
        if form.is_valid():
            print(form)
            form.save()
            messages.success(request, ("Sign up succesful"))
            username = request.POST.get("username")
            reg_number = username[0:4] + "/" + username[4:] 
            department = request.POST.get("department")
            print(request.POST)
            print(department, request.POST["department"])
            department = Department.objects.get(pk=department)
            user = User.objects.get(username=username)
            student = Student.objects.create(user=user, reg_no=reg_number,email=user.email, department=department)
            student.save()
            
            parent_phone_no = request.POST.get("parent-number")
            parent_user = User.objects.create_user(
                username="p" + username, password=reg_number, email=parent_email)
            parent_user.save()
            parent = Parent.objects.create(
                user=parent_user, phone_no =parent_phone_no ,email=parent_user.email)
            parent.save()
            student.parent = parent
            student.save()
            
            send_email_to_registered_users(parent_user.email,parent_user.username, reg_number)
            return HttpResponseRedirect(reverse("rst:login"))
        if form.errors:
            print("Form has errors")
            context = {
                'form': RegisterUserForm(),
                'errors': str(form.errors),
                'departments':departments
            }
            print(form.errors, form.error_messages)
            return render(request, 'rst/signup.html', context)

    return render(request, "rst/signup.html", context)

@staff_member_required
def search(request):
    if request.method == "POST":
        searched = request.POST.get("searched")
        students = Student.objects.filter(reg_no__contains=searched)
        context = {
            "searched":searched,
            "students":students
        }
        return render(request, "rst/search.html", context)
    context = {}
    return render(request, "rst/search.html", context)

@staff_member_required
def upload_result(request, student_id):
    student = Student.objects.get(id=student_id)
    courses = Course.objects.all().order_by("code").values()
    sessions = Session.objects.all()
    semesters = Semester.objects.all()
    levels = Level.objects.all()
    grades = Grade.objects.all()

    if request.method == "POST":
        print(request.POST)
        student = Student.objects.get(id=student_id)
        course_id = request.POST.get("course")
        course = Course.objects.get(id=course_id)
        grade_id = request.POST.get("grade")
        grade = Grade.objects.get(id=grade_id)
        semester_id = request.POST.get("semester")
        semester = Semester.objects.get(id=semester_id)
        session_id = request.POST.get("session")
        session = Session.objects.get(id=session_id)
        level_id = request.POST.get("level")
        level = Level.objects.get(id=level_id)
        exam_score = request.POST.get("exam-score")
        ca_score = request.POST.get("ca-score")
        try:
            result = Result.objects.get(student=student, course=course, session=session)
            if result:
                    context = {
                    "student": student,
                    "courses":courses,
                    "sessions": sessions,
                    "semesters": semesters,
                    "levels": levels,
                    "grades": grades,
                    "exists": "The student already has this result. You may go and update it"
                }
            return render(request, "rst/upload.html", context)

        except(Result.DoesNotExist):    
            result = Result.objects.create(
                student=student, course=course, grade=grade, semester=semester, 
                session=session, level=level, exam_score=exam_score, ca_score=ca_score)
            result.save()
            parent_email = student.parent.email
            send_email_for_newly_published_result(
                parent_email,student.user.first_name,course.code, grade)

            context = {
            "student": student,
            "courses":courses,
            "sessions": sessions,
            "semesters": semesters,
            "levels": levels,
            "grades": grades,
            "success": "Result upload Succesful"
            }
            return render(request, "rst/search.html", context)
    
    
    context = {
        "student": student,
        "courses":courses,
        "sessions": sessions,
        "semesters": semesters,
        "levels": levels,
        "grades": grades
    }
    return render(request, "rst/upload.html", context)

@login_required(login_url="rst:login")
def view_result(request):
    if request.user.username[0] == "p":
        parent = Parent.objects.get(user=request.user)
        student = parent.student_set.all()[0] 
    else:
        student = Student.objects.get(user=request.user)
    results = Result.objects.filter(student=student)
    levels = Level.objects.all()
    semesters = Semester.objects.all()
    print(results)
    context = {
        "student":student,
        "levels": levels,
        "semesters": semesters
    }
    return render(request, "rst/view_result.html", context)

@login_required(login_url="rst:login")
def view_level_result(request, level, semester):
    if request.user.username[0] == "p":
        parent = Parent.objects.get(user=request.user)
        student = parent.student_set.all()[0] 
    else:
        student = Student.objects.get(user=request.user)
    level = Level.objects.get(level=level)
    semester = Semester.objects.get(semester=semester)
    results = Result.objects.filter(student=student, level=level, semester=semester)
    print(results)

    try:
        result = results[0]
        
        context = {
            "student":student,
            "level": level,
            "results":results,
            "result":result,
            "semester": semester
        }
        return render(request, "rst/view_level_result.html", context)

    except(IndexError):    
        context ={
            "unavailable": "Results for this semester are unavailable"
        }
        return render(request, "rst/view_level_result.html", context)