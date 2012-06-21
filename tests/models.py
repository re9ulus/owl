from django.db import models
from djangotoolbox.fields import ListField, EmbeddedModelField
class Answer(models.Model):
	text = models.TextField()
	right = models.BooleanField()

# Create your models here.
class Question(models.Model):
	kind = models.CharField(max_length = 10)
	subject = models.CharField(max_length = 20)	
	theme = models.CharField(max_length = 20) 	
	text = models.TextField()					
	answers = ListField(EmbeddedModelField(Answer))

	def __unicode__(self):
		return self.__str__()

	def __str__(self):
		return self.text


class Quizz(models.Model):
	subject = models.CharField(max_length = 20)		
	theme = models.CharField(max_length = 20)		
	questions = ListField(EmbeddedModelField(Question))

class QuestionResult(models.Model):
	question = EmbeddedModelField(Question)
	answer = EmbeddedModelField(Answer)

class QuizzResult(models.Model):
	mark = models.IntegerField()
	quizz = EmbeddedModelField(Quizz)
	questions = ListField(EmbeddedModelField(QuestionResult))

# class User(models.Model):
# 	'''
# 	abstract class representing user of the system
# 	'''
# 	name = models.CharField(max_length=20)
# 	surname = models.CharField(max_length=30)
# 	email = models.CharField(max_length=30)
# 	password = models.CharField(max_length=30)
# 	pol = models.BooleanField()
# 	birthday = models.DateField()

# 	class Meta:
# 		abstract = True

# class Student(User):
# 	group = models.CharField(max_length=5)
# 	attempts = models.
# 	results = ListField(EmbeddedModelField(QuizzResult))