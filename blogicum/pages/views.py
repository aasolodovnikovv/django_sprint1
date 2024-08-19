from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def about(request: HttpRequest) -> HttpResponse:
    """О проекте."""
    return render(request, 'pages/about.html')


def rules(request: HttpRequest) -> HttpResponse:
    """Правила сайта."""
    return render(request, 'pages/rules.html')
