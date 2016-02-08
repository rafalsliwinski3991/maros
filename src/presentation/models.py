from django.db import models
from django.utils import timezone

# Create your models here.
class Postmod(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(
		default=timezone.now)
	published_date = models.DateTimeField(
		blank=True, null=True)
	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

class Tabormod(models.Model):
	machine = models.CharField(max_length=200)
	image_t = models.ImageField(upload_to='tabor', height_field='height_field', width_field='width_field')
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	def __str__(self):
		return self.machine

class Refmod(models.Model):
	name = models.CharField(max_length=200)
	image_r = models.ImageField(upload_to='referencje', height_field='height_field', width_field='width_field')
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	def __str__(self):
		return self.name
