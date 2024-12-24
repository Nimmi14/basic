# views.py
from django.shortcuts import render, HttpResponseRedirect,redirect,HttpResponse
from django.contrib.auth import authenticate, login, logout
from .models import Donar
from .forms import DonarForm,DonarLoginForm

def Donar_home(request):
    return render(request, 'mainapp/Home.html')

def Donar_signup(request):
    if request.method == 'POST':
        form = DonarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # return HttpResponse("Successfull you can login and donate")
            return HttpResponseRedirect('/ulogin/')  # Redirect to a success page or any desired URL
    else:
        form = DonarForm()
    return render(request, 'mainapp/signupform.html', {'form': form})
#
#
#

def Donar_login(request):
    if request.method == 'POST':
        form = DonarLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                patient = Donar.objects.get(username=username, password1=password)
                return HttpResponseRedirect('/ddash/')
            except Donar.DoesNotExist:
                return render(request, 'mainapp/loginform.html', {'form': form, 'error_message': 'Invalid username or password'})
    else:
        form = DonarLoginForm()
    return render(request, 'mainapp/loginform.html', {'form': form})





# def Donar_dashboard(request):
#     donar = Donar.objects.all()
#     return render(request, 'mainapp/userdashboard.html',{'donars':donar})


def Donar_dashboard(request):
    donar = None
    if request.user.is_authenticated:
        try:
            donar = Donar.objects.get(user=request.user)
            user_name=donar.username
            # Fetch Donar object for logged-in user
        except Donar.DoesNotExist:
            donar = None  # In case no Donar object is linked with this user
    return render(request, 'mainapp/userdashboard.html', {'donar': donar})