from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
        if request.method == 'POST':
                fname = request.POST['first_name']
                lname  = request.POST['last_name']
                uname = request.POST['user_name']
                email = request.POST['email']
                password = request.POST['password']
                conpassword = request.POST['conpassword']

                if password == conpassword:
                        if User.objects.filter(username = uname):
                                        messages.info(request,'Username already taken')
                                        return redirect('register')

                        elif User.objects.filter(email = email):
                                        messages.info(request,'Email id already registered')
                                        return redirect('register')
                        else:
                                user = User.objects.create_user(first_name = fname,last_name = lname, username = uname,email=email,password=password)
                                user.save()
                                return redirect('login')

                else:
                        messages.info(request, 'Password Mismatched')
                        return redirect('register')
        return render(request,'register.html')


def login(request):
        if request.method == 'POST':
                uname = request.POST['user_name']
                password = request.POST['password']

                user = auth.authenticate(username=uname, password=password)

                if user is not None:
                        auth.login(request, user)
                        return redirect('/')

                else:
                        messages.info(request, 'Invalid Credentials')
                        return redirect('login')
        return render(request, 'login.html')

def logout(request):
                auth.logout(request)
                return redirect('/')
