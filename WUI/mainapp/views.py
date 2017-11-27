from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import requests
from .forms import ContactForm


def index(request):
    title = 'Главная'
    sites = requests.get("http://shourick.pythonanywhere.com/sites").json()
    persons = requests.get("http://shourick.pythonanywhere.com/persons").json()
    return render(request, 'index.html', {'title': title, 'sites': sites, 'persons': persons})


def keywords(request):
    title = 'Ключевые слова'
    persons = requests.get("http://shourick.pythonanywhere.com/persons").json()
    keywords = requests.get("http://shourick.pythonanywhere.com/keywords").json()
    return render(request, 'keywords.html', {'title': title, 'persons': persons, 'keywords': keywords})


def support(request):
    title = 'Контакты'
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            sender = form.cleaned_data['sender']
            message = form.cleaned_data['message']
            copy = form.cleaned_data['copy']
            recipients = ['crowd.scoring@yandex.ru']
            # Если пользователь захотел получить копию себе, добавляем его в список получателей
            if copy:
                recipients.append(sender)
            try:
                send_mail(subject, message, 'crowd.scoring@yandex.ru', recipients)
            except BadHeaderError:  # Защита от уязвимости
                return HttpResponse('Invalid header found')
            return render(request, 'email/thanks.html', {'title': 'Спасибо'})
    else:
        form = ContactForm()
    return render(request, 'email/support.html', {'title': title, 'form': form})


@login_required
def general(request):
    title = 'Общая статистика'
    if request.method == 'POST':
        person_id = request.POST.get('person_id')
        url = "http://shourick.pythonanywhere.com/rank/" + str(person_id)
        ranks = requests.get(url).json()
        sites = requests.get("http://shourick.pythonanywhere.com/sites").json()
        return render(request, 'rank.html', {'title': title, 'ranks': ranks, 'sites': sites})
    else:
        persons = requests.get("http://shourick.pythonanywhere.com/persons").json()
        return render(request, 'general.html', {'title': title, 'persons': persons})


def rank(request):
    return render(request, 'rank.html')


@login_required
def daily(request):
    title = 'Ежедневная статистика'
    persons = requests.get("http://shourick.pythonanywhere.com/persons").json()
    sites = requests.get("http://shourick.pythonanywhere.com/sites").json()
    if request.method == 'POST':
        person_id = request.POST.get('person_id')
        site_id = request.POST.get('site_id')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        url = "http://shourick.pythonanywhere.com/rank/" + str(person_id) + '/' + str(site_id) + '/' + \
              str(start_date) + '&' + str(end_date)
        rank = requests.get(url).json()
        return render(request, 'rank_daily.html', {'title': title, 'ranks': rank})
    else:
        return render(request, 'daily.html', {'title': title, 'sites': sites, 'persons': persons})

