from django.shortcuts import render,HttpResponse,redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate,login

# Create your views here.
def anasayfa_view(request):
    return render(request, "anasayfa.html")

def giris_view(request):
    return render(request, "giris.html")

def kayit_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password1')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username,password=password)
        return redirect("home")
    return render(request,"kayit.html", {'form':form})