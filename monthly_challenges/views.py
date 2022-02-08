from django.shortcuts import redirect
from django.urls import reverse


def redirect_view(request):
    # redirect_path = reverse('month-challenge', args=['march'])
    # response = redirect(redirect_path)
    response = redirect('/challenges/')
    return response