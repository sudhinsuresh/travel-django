from django.shortcuts import render
from .models import Place,Team,MyUser
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    b=Place.objects.all()
    T=Team.objects.all()
    return render(request,'base.html',{'b':b,'T':T})


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('pass1')
        place = request.POST.get('place')
        number=request.POST.get('number')
        user = MyUser.objects.create_user(username=username, first_name=firstname, last_name=lastname, email=email, password=password,place=place,number=number)
        user.save()

    return render(request, 'signup.html')


@login_required
def handle_login(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('pass1')
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return home(request)
        else:
            messages.error(request,"Invalid Credentials")


    return render(request,'login.html')



def handle_logout(request):
    logout(request)
    return handle_login(request)



