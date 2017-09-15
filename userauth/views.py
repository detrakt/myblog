# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout as django_logout
from django.contrib.auth.models import User
from blog.models import Post

# Create your views here.
def index(request):
	return HttpResponse("User authentication module")

def auth(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			posts = Post.objects.all().order_by('-created_at')
			return render(request, 'posts.html', {'posts':posts, 'message': 'You successfully logged in'})
		else:
			return redirect('/users/error')
	elif request.method == 'GET':
		return render(request, 'login.html')

def error(request):
	return render(request, 'login.html', {'error': 'User and/or password are wrong.'})

def logout(request):
	if request.user.is_authenticated():
		django_logout(request)
	return redirect('/')

def register(request):
	if request.method=='GET':
		return render(request, 'register.html')
	elif request.method == 'POST':
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		try:
			user = User.objects.create_user(username=username, email=email, password=password)
			user.save()
		except:
			return render(request, 'register.html', {'error': 'Username and/or email already exist'})
		
		return redirect('/')
