from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string


monthly_challenges = {
    'january': 'Eat no meet for a month!',
    'february': 'Walk for at least 20 min for a day!',
    'march': 'Learn Django for 20 min everyday!',
    'april': 'Learn Javascript',
    'may': 'Learn Angular',
    'june': 'Dare to code',
    'july': 'Buy a new mac book pro',
    'august': 'Learn cloud technology',
    'september': 'Save water for future',
    'october': 'Donate blood!',
    'november': 'Water the plants',
    'december': 'Drink water regularly'
}

# Create your views here.

def index(request):
    list_items = ''
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse('month-challenge', args=[month])
        list_items += f'<li><a href="{month_path}">{capitalized_month}</a></li>'

    response_data = f'<ul>{list_items}</ul>'
    return HttpResponse(response_data)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, 'challenges/challenge.html')
        # response_data = render_to_string('challenges/challenge.html')
        # return HttpResponse(response_data)
    except:
        return HttpResponseNotFound('<h1>This month is not supported!</h1>')


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound('<h1>Invalid Month</h1>')

    redirect_month = months[month - 1]
    redirect_path = reverse('month-challenge', args=[redirect_month])   #  '/challenges/january'
    return HttpResponseRedirect(redirect_path)
