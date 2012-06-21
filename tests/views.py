# Create your views here.
from django.template import Context, loader
from django.http import HttpResponse
from django.core.context_processors import csrf
from django.utils import simplejson
from helpers import question_helper as question_h
from models import Answer

def many_ans(loads):
	'''
	parse answers for many_ans qyuestion
	'''
	#TODO:move to helpers
	answers = [Answer(text=i['text'], right=i['right']) for i in loads.get('answers',False)]
	return answers

def one_ans(loads):
	'''
	parse answers for one_ans question
	'''
	#TODO:move to helpers
	answers = [Answer(text=i, right=False) for i in loads.get('answers',False)]
	index = loads.get('right','')
	answers[index].right = True
	return answers

def text_ans(loads):
	'''
	parse answers for text_ans question
	'''
	#TODO:move to helpers
	answers = [Answer(text=i, right=True) for i in loads.get('answers',False)]
	return answers

def free_ans(loads):
	'''
	parse answers for free_ans questions
	'''
	#TODO:move to helpers
	return []

ans_parsers = {'one_ans': one_ans, 'many_ans' : many_ans, 
			'text_ans' : text_ans, 'free_ans' : free_ans}

def parse_question(loads):
	'''
	parse question by type
	'''
	#TODO:move to helpers
	res = {}
	res['kind'] = loads.get('type',False)
	res['subject'] = loads.get('subject',False)
	res['theme'] = loads.get('theme',False)
	res['text'] = loads.get('question',False)
	res['ans'] = []
	parser = ans_parsers.get(res['kind'],False)
	if parser:
		res['ans'] = parser(loads)
	return res

def parse(data):
	'''
	parse ajax question
	'''
	#TODO: Move to helpers
	loads = simplejson.loads(data)
	return parse_question(loads)

def validate(data):
	#TODO:test
	#TODO:move to helpers
	return data.kind and data.subject and data.theme and data.text and data.answers

def add_question(request):
	if request.is_ajax():
		params = parse(request.raw_post_data)
		if question_h.save_scratch(kind=params['kind'],
		 subject=params['subject'], theme=params['theme'],
		  text=params['text'], answers=params['ans']):
			return HttpResponse('accepted ' + str(params))
		else:
			return HttpResponse('fail')
	else:
		t = loader.get_template('add_question.html')
		c = Context()
		c.update(csrf(request))
		return HttpResponse(t.render(c))

def get_questions(request):
	#TODO Test
	t = loader.get_template('get_questions.html')
	c = Context()
	c.update(csrf(request))
	c['questions'] = question_h.get(subject = 'Math')
	return HttpResponse(t.render(c))