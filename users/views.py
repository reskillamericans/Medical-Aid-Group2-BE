from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.views.decorators.csrf import requires_csrf_token, csrf_protect
from aidApp.models import FAQ
from aidApp.helper import multiple_forms, newsletter_form


# Create your views here.

def index(request):
    return render(request, 'aidApp/index.html')

def about_us(request):
    return render(request, 'aidApp/about-us.html')

def faq(request):

    faqs = FAQ.objects.all()
    context = {
        "faqs": faqs
    }

    newsletter_form(request)

    return render(request, 'aidApp/faq.html', context)

@csrf_protect
def register(request):
    return render(request, 'users/register.html')

@csrf_protect
def submit_register_form(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        first_name = request.POST.get('fname', None)  
        last_name = request.POST.get('lname', None) 
        email = request.POST.get('email2', None)
        password = request.POST.get('cpwd', None)
        print(first_name, last_name)
        if User.objects.filter(email = email).exists():
            messages.info(request, 'Email already in use please use another one or login')
            return render(request, 'users/register.html') 
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request,user)
                messages.info(request, {'welcome': request.user.first_name})
                return render(request, 'aidApp/index.html')
            
    else:
        return render(request, 'users/register.html')

  
def render_login_page(request):
    return render(request, 'users/login.html')

def login_submit(request):
    username = request.POST['username']
    password = request.POST['pwd']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request,user)
        messages.info(request, {'welcome': request.user.username})
        return render(request, 'aidApp/index.html')
        
    else:
        return render(request, 'users/login.html')

def logout_view(request):
    logout(request)
    return redirect('users/login.html')
