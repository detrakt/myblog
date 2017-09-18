# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

def user_directory_path(instance, filename):
	return 'uploads/user_{0}/{1}'.format(instance.user.id, filename)

class ImgPost(models.Model):
	id = models.AutoField(primary_key=True)
	user = models.ForeignKey(User)
	image = models.ImageField(upload_to=user_directory_path)
	title = models.TextField(max_length=255, blank=False, null=False)
	description = models.TextField(max_length=255, blank=False, null=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now = True)
	likes = models.ManyToManyField(User, blank=True, related_name = 'post_likes')

	def __str__(self):
		return "%d %s" %(self.id, self.title)

class Like(models.Model):
	id = models.AutoField(primary_key=True)
	user_id = models.ForeignKey(User)
	post_id = models.ForeignKey(ImgPost)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now = True)

	def __str__(self):
		return "Like"

class Comment(models.Model):
	id = models.AutoField(primary_key=True)
	user_id=models.ForeignKey(User)
	post_id = models.ForeignKey(ImgPost)
	comment = models.TextField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now = True)

	def __str__(self):
		return "Comment"