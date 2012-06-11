parse_question = ->
	theme = $(':input#theme').val()
	subject = $(':input#subject').val()
	question = $(':input#question').val()
	res = 
		theme : theme
		subject : subject
		question : question

parse_classic_question = ->
	res = parse_question()
	tmp_ans = $(':input.answer')
	tmp_right = $(':input.right')

	answers = []
	for answer in tmp_ans
		q = $(answer).data 'a'
		answers[q] = 
			text : answer.value
			right : false

	for right in tmp_right
		if right.checked
			q = $(right).data 'a'
			answer[q].right = true

	res.answers = answers

	res = JSON.stringify res

# parse_input_question = ->
# 	#TODO: test
# 	res = parse_question()
# 	answers = $(':input.answer').value
# 	res.answers = answers
# 	return res

# parse_one_right_question = ->
# 	res = parse_question()
# 	answers = $(':input.answer').value


get_question_template = (val) ->
	"<div class='answer'><label>Answer #{val+1}:</label><br>
					<input type='text' class='answer' data-a='#{val}'>
					<input type='checkbox' class='right' data-a='#{val}'>
					</div>";

$(document).ready ->
	$('button#submit').click (event) ->
		event.preventDefault()
		res = parse_classic_question()
		console.log res
		$.ajax
			type: 'POST'
			contentType: 'application/json; charset=; utf-8'
			data: res
			success: (data) ->
				console.log('ajax success')
			error: ->
				console.log('ajax error')

	$('button#add').click (event) ->
		event.preventDefault()
		val = parseInt($(':input.answer:last').data('a'))+1
		if isNaN(val)
			val = 0
		template = get_question_template(val)
		$('div#control').before(template);

	$('button#remove').click (event) ->
		event.preventDefault()
		$('div.answer:last').remove()