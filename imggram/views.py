# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from models import ImgPost, Like, Comment
from forms import ImgForm
from datetime import datetime
from django.contrib.auth.models import User

def index(request):
	posts = ImgPost.objects.all().order_by("-created_at")
	return render(request, 'imggram_posts.html', {'posts':posts, 'title':'ImageGram'})

def show(request, post_id=-1):
	if post_id != -1:
		# Get post
		post = ImgPost.objects.get(id=post_id)
		
		#Get number of likes
		try:
			number_of_likes = Like.objects.filter(post_id=post).count()
		except:
			number_of_likes = 0
		
		#Get if user liked the current post
		try:
			user_post = Like.objects.get(user_id = request.user, post_id=post)
		except:
			user_post=None
		var = ""
		if user_post is not None:
			var = "y"
		else:
			var = "n"
		# End get if user liked the current post


		#Get the comments
		try:
			post_comments = Comment.objects.filter(post_id=post)
		except:
			post_comments = None

		return render(request, 'imggram_post.html', {'post':post, 'var':var, 'number_of_likes': number_of_likes, 'title':'ImageGram', 'comments':post_comments})
	else:
		return HttpResponse("Image not found")

def upload(request):	
	if request.method == 'POST':
		form = ImgForm(request.POST,request.FILES)
		if form.is_valid():
			post = form.save(commit=False)
			post.user = User.objects.get(id=request.user.id)
			post.save()
			return redirect("imggram_index")
		else:
			return HttpResponse("Invalid fields") 
	else:
		form = ImgForm()
		return render(request, 'imggram_new.html', {'form':form, 'title':'ImageGram - Upload image'})


def like_it(request):
	if request.method == 'POST':
		data = request.POST
		post_id = int(data['post_id'])
		post = ImgPost.objects.get(id=post_id)
		user = request.user
		
		query = Like.objects.filter(user_id=user, post_id=post)

		if not query.count():
			obj = Like.objects.create(user_id=user, post_id=post)
			obj.save()
			#return HttpResponse("y")
		else:
			Like.objects.filter(user_id=user, post_id=post).delete()
			#return HttpResponse("n")
	return HttpResponse(Like.objects.filter(post_id = post).count())
		#if user not in post.likes:
		#	post.likes.add(user)

	#return HttpResponse("Ok")

def comment_it(request):
	if request.method=='POST':
		data = request.POST
		user = request.user
		comment = data['comment']
		post_id = int(data['post-id-comment'])
		post = ImgPost.objects.get(id=post_id)
		if comment is not None:
			new_comment = Comment.objects.create(user_id=request.user, comment=comment, post_id=post)
			new_comment.save()
			
		return redirect("/imggram/show/%d/"%post_id)

def delete_comment(request, post_id, comment_id):
	Comment.objects.get(id=comment_id).delete()
	return redirect("/imggram/show/%d/" %int(post_id))