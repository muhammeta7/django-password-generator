from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
	return render(request, 'generator/home.html')

def password(request):
	characters = list('abcedefghijklmnopqrstuvwxyz')
	length = 10
	the_password = ''

	for i in range(length):
		the_password += random.choice(characters)

	return render(request, 'generator/password.html', {'password': the_password})