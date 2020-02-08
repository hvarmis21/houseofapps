from django.shortcuts import render,HttpResponse,redirect
from .forms import RegisterForm,LoginForm
from django.contrib.auth import authenticate,login, logout
import requests
import json
# Create your views here.
def home_view(request):
    if request.method == "POST":
        if request.POST["search_list"]:
            return redirect("/search/{}".format(request.POST["search_list"]))
    if request.user.is_authenticated:
        response = requests.get('https://api.nasa.gov/planetary/apod?api_key=pdA7MvW4yL8zwmgyKHz3BnM8WRKR715bFowEYiU8')
        return render(request, "anasayfa.html", {"response": response.json()})
    else:
        return render(request, "anasayfa.html")

def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect("home")
    return render(request, "giris.html",{'form':form})

def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password1')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username,password=password)
        return redirect("home")
    return render(request, "kayit.html", {'form': form})


def logout_view(request):
    logout(request)
    return redirect("home")

def search_view(request,search_word):
    response = requests.get('https://images-api.nasa.gov/search?q={}'.format(search_word))
    items = []
    for item in response.json()['collection']['items'][:5]:
        items.append({'link': item['links'][0]['href'], 'data': item['data'][0]['photographer'],
                      'description': item['data'][0]['description']})

    return render(request, "search.html", {'response': items})
