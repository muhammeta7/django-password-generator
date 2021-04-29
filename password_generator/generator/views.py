from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
	return render(request, 'generator/home.html')

def password(request):
	characters = list('abcedefghijklmnopqrstuvwxyz')

	if request.GET.get('uppercase'):
		characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXY'))
	if request.GET.get('special'):
		characters.extend(list('!@#$%^&*(){}[]'))
	if request.GET.get('numbers'):
		characters.extend(list('1234567890'))

	length = int(request.GET.get('length'))
	the_password = ''

	for i in range(length):
		the_password += random.choice(characters)

	return render(request, 'generator/password.html', {'password': the_password})