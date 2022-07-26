"""samplesite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.http import HttpRequest, HttpResponse
import random


chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"


def homepage(request):
    return HttpResponse(':(: Смайл Шредінгера. Одночасно веселий та сумний')


def user_password(request, password):
    for i in password:
        if i not in chars:
            return HttpResponse("Пароль має містити лише букви латинського алфавіта у будь якому регістрі або цифри ")
    if len(password) != 8:
        return HttpResponse("Пароль має бути завдовшки 8 символів")
    else:
        return HttpResponse(f'Пароль: {password} відповідає параметрам')


def generate_password(request, length):
    password = ""
    length = int(length)
    for j in range(length):
        password += random.choice(chars)
    return HttpResponse(f'Пароль: {password}')


def article(request, article_id, article_slug):
    response = f' Номер статі: {article_id} Заголовок: {article_slug}'
    return HttpResponse(response)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage', homepage),
    path('home', homepage),
    path('', homepage),
    path('password/<password>', user_password),
    path('password/generate/<length>', generate_password),
    path('article/<int:article_id>/<slug:article_slug>', article),
]
