from django.shortcuts import render, get_object_or_404
from django.utils import timezone

def main_page(request):
    return render(request, 'webapp/Main_page.html')

def login(request):
    return render(request, 'webapp/Login_page.html')

# Create your views here.
