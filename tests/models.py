from django.db import models
from djangotoolbox.fields import ListField

class Answer:
	def __init__(self, text, is_true):
		self.text = text
		self.is_true = is_true

# Create your models here.
class Questions(models.Model):
	text = models.TextField()
	theme = models.CharField(max_length = 100)
	answers = ListField()