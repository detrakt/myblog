# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from models import ImgPost

def index(request):
	posts = ImgPost.objects.all().order_by("-created_at")
	return render(request, 'imggram_posts.html', {'posts':posts})

def show(request, post_id=-1):
	if post_id != -1:
		post = ImgPost.objects.get(id=post_id)
		return render(request, 'imggram_post.html', {'post':post})
	else:
		return HttpResponse("Image not found")
