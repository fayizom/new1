from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from app1.forms import CustomUserCreationForm
def home(request):
    return render(request,'home.html')
def adminhome(request):
    return render(request,'adminhome.html')
def studenthome(request):
    return render(request,'studenthome.html')
def teacherhome(request):
    return render(request,'teacherhome.html')


def studentsignup(request):
    form=CustomUserCreationForm()
    if(request.method=="POST"):
        form=CustomUserCreationForm(request.POST)
        if(form.is_valid()):
            f=form.save(commit=False)
            f.is_student=True
            f.save()
            return home(request)
    return render(request,'studentsignup.html',{'form':form})
def teachersignup(request):
    form=CustomUserCreationForm()
    if(request.method=="POST"):
        form=CustomUserCreationForm(request.POST)
        if(form.is_valid()):
            f=form.save(commit=False)
            f.is_teacher=True
            f.save()
            return home(request)
    return render(request,'teachersignup.html',{'form':form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user= authenticate(username=username, password=password)
        if user and user.is_superuser == True:
            login(request,user)
            return adminhome(request)
        elif user and user.is_student == True:
            login(request, user)
            return studenthome(request)
        elif user and user.is_teacher == True:
            login(request, user)
            return teacherhome(request)
        else:
            return HttpResponse("Invalid login details.....")

    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return home(request)
