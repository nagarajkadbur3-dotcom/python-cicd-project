from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("""
        <h1>Python CI/CD Project</h1>
        <h2>Welcome to My Python Application</h2>
        <p>Deployed using Jenkins CI/CD.</p>
    """)