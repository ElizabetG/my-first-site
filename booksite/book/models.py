from django.db import models
from django.utils import timezone

class Book(models.Model):
	title = models.CharField(max_length=200)
	about = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	image_path = models.CharField(max_length=200)
	pdf_path = models.CharField(max_length=200)
	rating = models.IntegerField()

def publish(self):
	self.published_date = timezone.now()
	self.save()

def __str__(self):
	return self.title