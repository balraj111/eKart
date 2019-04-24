from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm,RegisterForm



def home_page(request):
    contact=ContactForm(request.POST or None)
    context={
        "title":"first app",
        "form" : contact
    }

    if contact.is_valid():
        print(contact.cleaned_data)


    # if request.method == "POST":
    #     print(request.POST.get('fullname'))
    #     print(request.POST.get('email'))
    #     print(request.POST.get('content'))

    return render(request,'home.html',context)

def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "title": "register page",
        "s_form": form
    }
    #print(request.POST)
    if request.method == "POST":



        print(form.is_valid())
        if form.is_valid():
            user = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password1')
            print('valid')
            new_user = User.objects.create_user(user, email, password)
            print(new_user)

            print(form.cleaned_data)
        else:

            print('invalid form')
            # user = request.POST.get('Username')
            # email = request.POST.get('Email')
            # password = request.POST.get('password1')
            # new_user = User.objects.create_user(user, email, password)
            # print(new_user)



    return render(request, 'register.html', context)


def login_page(request):
    if request.method == "POST":
        s_form=RegisterForm(request.POST)

    else:
        s_form = RegisterForm(request.POST)

    context = {
        "title": "first app",
        "s_form": s_form
    }
    print(len(request.POST))
    if request.method == "POST":
        if len(request.POST)==7:
            if s_form.is_valid():

                user=request.POST.get('usr')
                email=request.POST.get('email')
                password=request.POST.get('psw')
                new_user=User.objects.create_user(user,email,password)
                print(new_user)
        print(request.user.is_authenticated())
        print(request.POST.get('usr'))
        print(request.POST.get('psw'))
        print(request.POST.get('flag'))
        user=authenticate(request,username=request.POST.get('uname'),password=request.POST.get('psw'))
        if user is not None:
            login(request,user)
            print('login')
        else:
            print('error')

    return render(request,'login.html',context)



