from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .forms import UserCreateForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .decorators import unauthenticated_user, admin_only
from django.contrib.auth.models import Group


#Account function
@unauthenticated_user
def register(request):
    
    form = UserCreateForm()
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data.get('username')
            user.save()
            group = Group.objects.get(name='user')
            user.groups.add(group)
            
            messages.success(request, 'Account successfully created for ' + username)
            return HttpResponseRedirect(reverse('keny:user_login'))
            
        else:
            messages.error(request, form.errors)
            
    return render(request, 'account/register.html', {'form':form})

@unauthenticated_user
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            messages.error(request, 'Username OR Password not correct!')
            
    return render(request, 'account/login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
    
    
#Acccount page
@login_required
@admin_only
def index(request):
    return render(request, 'account/index.html')
    
@login_required
def user_page(request):
    context = {}
    return render(request, 'account/user_page.html', context)
    
    
@login_required
def subject_page(request):
    context = {}
    return render(request, 'account/subjects.html', context)
    
@login_required
def attendance_page(request):
    context ={}
    return render(request, 'account/attendance_page.html', context)

@login_required
def classDetail(request, id):
    context = {}
    return render(request, 'account/submit_attendance.html', context)