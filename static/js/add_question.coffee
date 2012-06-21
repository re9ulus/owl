#ToDo: There must be checked in one_ans question

parse =
	_question : ->	
		type = $(':input#type').val()
		theme = $(':input#theme').val()
		subject = $(':input#subject').val()
		question = $(':input#question').val()
		res = 
			theme : theme
			subject : subject
			question : question
			type : type

	many_ans : ->
		res = @_question()
		tmp_ans = $(':input.answer')
		tmp_right = $(':input.right')
		answers = []
		for answer in tmp_ans
			q = $(answer).data 'a'
			answers[q] = 
				text : answer.value
				right : false
		res.answers = answers
		JSON.stringify res

	one_ans : ->
		res = @_question()
		right = $(':input.right:checked').data('a')
		tmp_ans = $(':input.answer')
		answers = []
		for answer in tmp_ans
			answers.push answer.value
		res.answers = answers
		res.right = right
		JSON.stringify res

	text_ans : ->
		#TODO:test
		res = @_question()
		tmp_ans = $(':input.answer')
		answers = []
		for answer in tmp_ans
			answers.push answer.value
		res.answers = answers
		JSON.stringify res

	free_ans : -> 
		res = @_question()
		JSON.stringify res

ans_types =
	many_ans : "many_ans"
	one_ans : "one_ans"
	text_ans : "text_ans"
	free_ans : "free_ans"

get_ans_template = (type, val) ->
	switch type
		when "many_ans" then "<div class='answer'>
				<label>Answer #{val+1}:</label><br>
				<input type='text' class='answer' data-a='#{val}'>
				<input type='checkbox' class='right' data-a='#{val}'>
			</div>"
		when "one_ans" then "<div class='answer'>
				<label>Answer #{val+1}:</label><br>
				<input type='text' class='answer' data-a='#{val}'>
				<input type='radio' name='ans_group' class='right' data-a='#{val}'>
			</div>"
		when "text_ans" then "<div class='answer'>
				<label>Answer #{val+1}:</label><br>
				<input type='text' class='answer' data-a='#{val}'>
			</div>"
		when "free_ans" then ""
		else ""

render_ans = (type, val) ->
	$('div#answers').append(get_ans_template(type,val))

change_ans_type = (type) ->
	$('div#answers').empty()
	render_ans(type, 0)

$(document).ready ->
	_type = ans_types.many_ans

	change_ans_type(_type)

	$(':input#type').change ->
		val = $(@).val()
		_type = ans_types[val]
		if _type == undefined
			_type = ans_types.many_ans
		change_ans_type(_type)

	$('button#submit').click (event) ->
		event.preventDefault()
		res = parse[_type]()
		console.log res
		$.ajax
			type: 'POST'
			contentType: 'application/json; charset=utf-8;'
			data: res
			success: (data) ->
				console.log('ajax success')
				console.log(data)
			error: ->
				console.log('ajax error')

	$('button#add').click (event) ->
		event.preventDefault()
		if _type != ans_types.free_ans
			val = parseInt($(':input.answer:last').data('a'))+1
			if isNaN(val)
				val = 0
			render_ans(_type,val)

	$('button#remove').click (event) ->
		event.preventDefault()
		$('div.answer:last').remove()