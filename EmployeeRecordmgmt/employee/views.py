from django.shortcuts import render ,redirect
from .models import *
from django.contrib.auth import login,logout,authenticate
# Create your views here.
def index(request):
    return render(request,'index.html')

def registration(request):
    error= ""
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        ec = request.POST['employeecode']
        em = request.POST['emailid']
        pwd = request.POST['password']
        try:
            user = User.objects.create_user(first_name=fn,last_name=ln,username=em,password=pwd)
            EmployeeDetail.objects.create(user=user)
            EmployeeExperiance.objects.create(user=user)
            EmployeeEducation.objects.create(user=user)

            error="No"
        except:
            error="Yes"

        
    return render(request,'registration.html',locals())


def emplogin(request):
    error = ""
    if request.method == "POST":
        u = request.POST['email']
        p = request.POST['pwd']
        user = authenticate(username=u,password=p)
        if user:
            login(request,user)
            error="No"
        else:
            error="Yes"    
    return render(request,'emplogin.html',locals())

def emp_home(request):
    if not request.user.is_authenticated:
        return redirect('emplogin')
    return render(request,'emp_home.html')



def Logout(request):
    logout(request)
    return redirect('index')

def profile(request):
    if not request.user.is_authenticated:
        return redirect('emplogin')
    error = ""
    user = request.user
    employee = EmployeeDetail.objects.get(user=user)
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        dept = request.POST['department']
        designation = request.POST['designation']
        contact = request.POST['contact']
        jdate = request.POST['jdate']
        gender = request.POST['gender']

        employee.user.first_name=fn
        employee.user.last_name=ln
        employee.empdept=dept
        employee.designation=designation
        employee.contact=contact
        employee.gender=gender

        if jdate:
            employee.joiningdate = jdate

        try:
            employee.save()
            employee.user.save()
            error="No"
        except:
            error="Yes"
    return render(request,'profile.html',locals())


def myexperience(request):
    if not request.user.is_authenticated:
        return redirect('emplogin')
    user = request.user
    experience = EmployeeExperiance.objects.get(user=user)
    
    return render(request,'myexperience.html',locals())

def edit_myexperience(request):
    if not request.user.is_authenticated:
        return redirect('emplogin')
    error = ""
    user = request.user
    experience = EmployeeExperiance.objects.get(user=user)
    if request.method == "POST":
        company1name = request.POST['company1name']
        company1designation = request.POST['company1designation']
        company1salary = request.POST['company1salary']
        company1duration = request.POST['company1duration']

        company2name = request.POST['company2name']
        company2designation= request.POST['company2designation']
        company2salary = request.POST['company2salary']
        company2duration = request.POST['company2duration']

        company3name = request.POST['company3name']
        company3designation = request.POST['company3designation']
        company3salary = request.POST['company3salary']
        company3duration = request.POST['company3duration']


        experience.company1name=company1name
        experience.company1designation=company1designation
        experience.company1salary=company1salary
        experience.company1duration=company1duration

        experience.company2name=company2name
        experience.company2designation=company2designation
        experience.company2salary=company2salary
        experience.company2duration=company2duration

        experience.company3name=company3name
        experience.company3designation=company3designation
        experience.company3salary=company3salary
        experience.company3duration=company3duration

        try:
            experience.save()
        
            error="No"
        except:
            error="Yes"
    return render(request,'edit_myexperience.html',locals())


def my_education(request):
    if not request.user.is_authenticated:
        return redirect('emplogin')
    user = request.user
    education = EmployeeEducation.objects.get(user=user)
    
    return render(request,'my_education.html',locals())

def edit_myeducation(request):
    if not request.user.is_authenticated:
        return redirect('emplogin')
    error = ""
    user = request.user
    education = EmployeeEducation.objects.get(user=user)
    if request.method == "POST":
        coursepg = request.POST['coursepg']
        schoolclgpg = request.POST['schoolclgpg']
        yearpassingpg = request.POST['yearpassingpg']
        percentagepg = request.POST['percentagepg']

        coursegra = request.POST['coursegra']
        schoolclggra= request.POST['schoolclggra']
        yearpassinggra = request.POST['yearpassinggra']
        percentagegra = request.POST['percentagegra']

        coursessc = request.POST['coursessc']
        schoolclgssc = request.POST['schoolclgssc']
        yearpassingssc = request.POST['yearpassingssc']
        percentagessc = request.POST['percentagessc']

        coursehsc = request.POST['coursehsc']
        schoolclghsc = request.POST['schoolclghsc']
        yearpassinghsc = request.POST['yearpassinghsc']
        percentagehsc = request.POST['percentagehsc']


        education.coursepg=coursepg
        education.schoolclgpg=schoolclgpg
        education.yearpassingpg=yearpassingpg
        education.percentagepg=percentagepg

        education.coursegra=coursegra
        education.schoolclggra=schoolclggra
        education.yearpassinggra=yearpassinggra
        education.percentagegra=percentagegra

        education.coursessc=coursessc
        education.schoolclgssc=schoolclgssc
        education.yearpassingssc=yearpassingssc
        education.percentagessc=percentagessc

        education.coursehsc=coursehsc
        education.schoolclghsc=schoolclghsc
        education.yearpassinghsc=yearpassinghsc
        education.percentagehsc=percentagehsc

        try:
            education.save()
        
            error="No"
        except:
            error="Yes"
    return render(request,'edit_myeducation.html',locals())


def change_password(request):
    if not request.user.is_authenticated:
        return redirect('emplogin')
    error = ""
    user = request.user
    if request.method == "POST":
        c =request.POST['currentpassword']
        n =request.POST['newpassword']
        try:
            if user.check_password(c):
                user.set_password(n)
                user.save()
                error="No"
            else:
                error="Not"    
        except:
            error="Yes"
    return render(request,'change_password.html',locals())


def admin_login(request):
    error = ""
    if request.method == "POST":
        u = request.POST['username']
        p = request.POST['pwd']
        user = authenticate(username=u,password=p)
        try:
            if user.is_staff:
                login(request,user)
                error="No"
            else:
                error="Yes"  
        except:
            error="Yes"          
    return render(request,'admin_login.html',locals())


def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    return render(request,'admin_home.html')


def change_passwordadmin(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    user = request.user
    if request.method == "POST":
        c =request.POST['currentpassword']
        n =request.POST['newpassword']
        try:
            if user.check_password(c):
                user.set_password(n)
                user.save()
                error="No"
            else:
                error="Not"    
        except:
            error="Yes"
    return render(request,'change_passwordadmin.html',locals())

def all_employee(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    employee = EmployeeDetail.objects.all()
    return render(request,'all_employee.html',locals())

def delete_employee(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    user= User.objects.get(id=pid)
    user.delete()
    return redirect('all_employee')

def edit_profile(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    user = User.objects.get(id=pid)
    employee = EmployeeDetail.objects.get(user=user)
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        dept = request.POST['department']
        designation = request.POST['designation']
        contact = request.POST['contact']
        jdate = request.POST['jdate']
        gender = request.POST['gender']

        employee.user.first_name=fn
        employee.user.last_name=ln
        employee.empdept=dept
        employee.designation=designation
        employee.contact=contact
        employee.gender=gender

        if jdate:
            employee.joiningdate = jdate

        try:
            employee.save()
            employee.user.save()
            error="No"
        except:
            error="Yes"
    return render(request,'edit_profile.html',locals())


def edit_education(request,pid):
    if not request.user.is_authenticated:
        return redirect('emplogin')
    error = ""
    user = User.objects.get(id=pid)
    education = EmployeeEducation.objects.get(user=user)
    if request.method == "POST":
        coursepg = request.POST['coursepg']
        schoolclgpg = request.POST['schoolclgpg']
        yearpassingpg = request.POST['yearpassingpg']
        percentagepg = request.POST['percentagepg']

        coursegra = request.POST['coursegra']
        schoolclggra= request.POST['schoolclggra']
        yearpassinggra = request.POST['yearpassinggra']
        percentagegra = request.POST['percentagegra']

        coursessc = request.POST['coursessc']
        schoolclgssc = request.POST['schoolclgssc']
        yearpassingssc = request.POST['yearpassingssc']
        percentagessc = request.POST['percentagessc']

        coursehsc = request.POST['coursehsc']
        schoolclghsc = request.POST['schoolclghsc']
        yearpassinghsc = request.POST['yearpassinghsc']
        percentagehsc = request.POST['percentagehsc']


        education.coursepg=coursepg
        education.schoolclgpg=schoolclgpg
        education.yearpassingpg=yearpassingpg
        education.percentagepg=percentagepg

        education.coursegra=coursegra
        education.schoolclggra=schoolclggra
        education.yearpassinggra=yearpassinggra
        education.percentagegra=percentagegra

        education.coursessc=coursessc
        education.schoolclgssc=schoolclgssc
        education.yearpassingssc=yearpassingssc
        education.percentagessc=percentagessc

        education.coursehsc=coursehsc
        education.schoolclghsc=schoolclghsc
        education.yearpassinghsc=yearpassinghsc
        education.percentagehsc=percentagehsc

        try:
            education.save()
        
            error="No"
        except:
            error="Yes"
    return render(request,'edit_education.html',locals())


def edit_experience(request,pid):
    if not request.user.is_authenticated:
        return redirect('emplogin')
    error = ""
    user = User.objects.get(id=pid)
    experience = EmployeeExperiance.objects.get(user=user)
    if request.method == "POST":
        company1name = request.POST['company1name']
        company1designation = request.POST['company1designation']
        company1salary = request.POST['company1salary']
        company1duration = request.POST['company1duration']

        company2name = request.POST['company2name']
        company2designation= request.POST['company2designation']
        company2salary = request.POST['company2salary']
        company2duration = request.POST['company2duration']

        company3name = request.POST['company3name']
        company3designation = request.POST['company3designation']
        company3salary = request.POST['company3salary']
        company3duration = request.POST['company3duration']


        experience.company1name=company1name
        experience.company1designation=company1designation
        experience.company1salary=company1salary
        experience.company1duration=company1duration

        experience.company2name=company2name
        experience.company2designation=company2designation
        experience.company2salary=company2salary
        experience.company2duration=company2duration

        experience.company3name=company3name
        experience.company3designation=company3designation
        experience.company3salary=company3salary
        experience.company3duration=company3duration

        try:
            experience.save()
        
            error="No"
        except:
            error="Yes"
    return render(request,'edit_experience.html',locals())
