from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

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


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound('This month is not supported!')


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound('Invalid Month')

    redirect_month = months[month - 1]
    return HttpResponseRedirect('/challenges/' + redirect_month)
