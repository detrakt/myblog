# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from models import Post
# Create your views here.

def index(request):
	posts = Post.objects.all().order_by('-created_at')
	return render(request, 'posts.html', {'posts': posts})

def about(request):
	return render(request, 'about.html')

def createpost(request):
	if request.method=='GET':
		return render(request, 'createpost.html')
	else:
		title = request.POST['title']
		content = request.POST['content']
		post = Post.objects.create(title=title, content=content)
		return redirect('/')

def deletepost(request, post_id = -1):
	if post_id!=-1:
		post = Post.objects.get(id=post_id)
		post.delete()
		return redirect('/')

