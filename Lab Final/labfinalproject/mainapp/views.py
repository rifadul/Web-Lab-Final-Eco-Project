from django.shortcuts import render, HttpResponseRedirect
from .form import Signupform, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import ProductDetail
from django.contrib.auth.models import User

# Create your views here.


def home(request):
    product = ProductDetail.objects.all()
    # product = ProductDetail.objects.filter(product_category='Grocery')
    context = {
        'active': 'active',
        'products': product,
    }
    return render(request, 'mainapp/home.html', context)


def antiseptic(request):
    product = ProductDetail.objects.filter(product_category=1)
    return render(request, 'mainapp/antiseptic.html', {'products': product})


def grocery(request):
    product = ProductDetail.objects.filter(product_category=2)
    return render(request, 'mainapp/grocery.html', {'products': product})


def bags(request):
    product = ProductDetail.objects.filter(product_category=3)
    return render(request, 'mainapp/antiseptic.html', {'products': product})


def shoes(request):
    product = ProductDetail.objects.filter(product_category=4)
    return render(request, 'mainapp/antiseptic.html', {'products': product})


def productDetails(request, id):
    product = ProductDetail.objects.get(id=id)
    return render(request, 'mainapp/productDetails.html', {'product': product})


def userlogin(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            forms = LoginForm(request=request, data=request.POST)
            if forms.is_valid():
                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(
                    request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/')
            else:
                messages.error(request, 'Enter valid username and password')
        else:
            forms = LoginForm()
        return render(request, 'mainapp/login.html', {'forms': forms})
    else:
        return HttpResponseRedirect('/')


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/login/')
    else:
        return HttpResponseRedirect('/')


def usersignup(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            forms = Signupform(request.POST)
            if forms.is_valid():
                messages.success(request, 'Account Create Successfully')
                forms.save()
                forms = Signupform()
        else:
            forms = Signupform()
        return render(request, 'mainapp/signup.html', {'forms': forms})
    else:
        return HttpResponseRedirect('/')


def profile(request):
    if request.user.is_authenticated:
        return render(request, 'mainapp/profile.html')
    else:
        return HttpResponseRedirect('/login/')
