from django.shortcuts import render
from django.shortcuts import render, Http404, get_object_or_404, HttpResponseRedirect
import os
from django.contrib import auth
# Create your views here.


# тут можно будет изменить название сайта
def name_site():
    site_name = 'World of Photos'
    return site_name


def index(request):
    site_name = name_site()
    menu_item = 'Главная'
    return render(request, 'index.html',  {'site_name': site_name, 'razdel_menu':menu_item})


# Передеам пути к файлам, т.к. в бд будут лежать пути до изображений
# (изображения хпанить в БД не гуд, вынесем их на NAS хранилище)
def home_gal(request):
    menu_item = 'Галлерея'
    gallery = './static/img'
    gallerys = os.listdir(gallery)
    #gallerys = os.path.abspath(gallerys)
    for i in gallerys:
        print(os.path.relpath(i))
    return render(request, 'gallerey.html', {'site_name': name_site(),
                                             'razdel_menu': menu_item,
                                             'gallereys': gallerys})


def photograf(request):
    menu_item = 'Фотографы (страница на стадии разработки)'
    return render(request, 'index.html', {'site_name': name_site(), 'razdel_menu': menu_item})


def contacts(request):
    menu_item = 'Наши контакты'
    return render(request, 'index.html', {'site_name': name_site(), 'razdel_menu': menu_item})


def login(request):
    if request.method == 'POST':
        print ("POST data =", request.POST)
        username = request.POST.get('login')
        password = request.POST.get('password')
        user = auth.authenticate(username = username, password = password)
        print(user)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect('/')
        else:
            return render(request, 'index.html',{'username': username, 'errors': True})


def logout(request):
    auth.logout(request)
    # Перенаправление на страницу.
    return HttpResponseRedirect("/")
