from datetime import datetime as dt
from django.http import HttpResponse
from django.shortcuts import render, reverse
import os


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать список файлов рабочей директории': reverse('workdir')
    }
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    current_time = dt.now().time().strftime('%H:%M:%S')
    msg = f'<h2>Текущее время: {current_time}</h2>'
    return HttpResponse(msg)


def workdir_view(request):
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей 
    # директории
    files = ''
    for item in os.listdir():
        if os.path.isfile(item):
            files = f'{files}<br>{item}'
    return HttpResponse(f'<h2>{files}</h2>')
