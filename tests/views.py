# Create your views here.
from django.template import Context, loader
from django.http import HttpResponse
from django.core.context_processors import csrf
from django.utils import simplejson
import question_helper as question_h
from models import Answer

def add_question(request):
	if request.is_ajax():
		loads = simplejson.loads(request.raw_post_data)
		subject = loads.get('subject',False)
		theme = loads.get('theme',False)
		text = loads.get('text',False) 
		answers = [Answer(text=i['text'], right=i['right']) for i in loads.get('answers',False)]
		#if question_h.save(kind='classic', subject=subject, theme=theme, text=text, answers=answers):
		return HttpResponse('Win!!!')
		#else:
		#	return HttpResponse('Fail')
	else:
		t = loader.get_template('add_question.html')
		c = Context()
		c.update(csrf(request))
		return HttpResponse(t.render(c))