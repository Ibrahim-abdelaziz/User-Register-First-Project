from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import Staff_form
from .models import staff,info
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def index(request) :
    return HttpResponse("Hello Project")

def register(request):
    form=Staff_form(request.POST or None , request.FILES)
    obj=staff()
    if form.is_valid():
        obj.name=form.cleaned_data['name']
        obj.email=form.cleaned_data['email']
        obj.age=form.cleaned_data['age']
        obj.birthday=form.cleaned_data['birthday']
        obj.img=form.cleaned_data['img']
        obj.save()
        return HttpResponseRedirect('/forms/notes')
    return render(request,'register.html',{'form':form})

def edit_register(request,id):
    form = Staff_form(request.POST or None)
    obj = staff.objects.get(id=id)
    if form.is_valid():
        obj.name = form.cleaned_data['name']
        obj.email = form.cleaned_data['email']
        obj.age = form.cleaned_data['age']
        obj.birthday = form.cleaned_data['birthday']
        obj.save()
        return HttpResponseRedirect('/forms/notes')
    return render(request, 'edit_register.html',{'form':form})

def delete_register(request,id):
    obj = staff.objects.get(id=id)
    obj.delete()
    return HttpResponseRedirect('/forms/notes')


def notes(request):
    note=staff.objects.all()

    return render(request,'home.html',{'note':note})
def one_note(request,id):
    notee=staff.objects.get(id=id)

    return render(request,'one_note.html',{'notee':notee})


#################################
  #                Register     #
#################################
def registerr(request):
    return render(request,'register_user.html',{})
def register_user(request):
    try:
        user = User.objects.create_user(request.POST['username'],request.POST['email'],request.POST['password'])
        user.first_name=request.POST['first_name']
        user.last_name=request.POST['last_name']
        user.save()
        return HttpResponseRedirect('/forms')
    except:
        return HttpResponse('User Is Exist')
#################################
 #  Log in / profile / log out  #
#################################
def log (request):
    return render(request,'log.html',{})
def profile(request,username):
    return render(request,'profile.html',{'username':username})
def log_user(request):
    username=request.POST['username']
    password=request.POST['password']
    result=authenticate(username=username,password=password)
    if result is not None:
        login(request,result)
        link='/forms/profile/' + str(result)
        return HttpResponseRedirect(link)
    else:
        return HttpResponse('user is exist')

def logout_user(request):
    logout(request)
    return HttpResponse(' log out ')
##########################################################
def log_info(request,username):
    return render(request,'log_info.html',{'username':username})
def loginfo_backend(request,username):
    u=info()
    user=User.objects.get(username=username)
    u.jobs=request.POST['jobs']
    u.lang=request.POST['lang']
    u.num=request.POST['num']
    u.username=user
    u.save()
    return HttpResponse(' Yes I am')
def show_user(request,username):
    user=User.objects.get(username=username)
    inf=info.objects.filter(username=user)

    context = {'n':user, 'm':inf}

    return render(request,'show.html',context)