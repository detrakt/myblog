# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Post(models.Model):
	id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=255, blank=False, null=False)
	content = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title
	
	def create(self, title, content):
		self.title = title
		self.content = content
		self.save()