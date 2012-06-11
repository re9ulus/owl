//not used
//refactored in add_question.coffee

function parse_classic_question(){
	var theme = $(':input#theme').val();
	var subject = $(':input#subject').val();
	var question = $(':input#question').val();
	var _answers = $(':input.answer');
	var _rights = $(':input.right');

	var answers = [];
	var q = 0;

	for(var i = 0; i<_answers.length; ++i)
	{
		q = $(_answers[i]).data('a');
		answers[q] = {text: _answers[i].value, right: false};
	}

	for (var i = 0; i<_rights.length; ++i){
		if( _rights[i].checked ){
			q = $(_rights[i]).data('a');
			answers[q].right = true;
		}
	}
	var res = {
		subject : subject,
		theme : theme,
		question : question,
		answers : answers
	};

	res = JSON.stringify(res)

	return res;
}

$(document).ready(
	function(){
		$('button#submit').click(function(event){
			event.preventDefault();
			var res = parse_classic_question();
			console.log(res);
			$.ajax({
				//url: 'localhost:8000/add_question'
				type: "POST",
				contentType: "application/json; charset=utf-8",
				data:res,
				success: function(data){
					alert(data);
					console.log('Win!!!');
				},
				error: function(){
					console.log('Fail');
				}
			});
		});

		$('button#add').click(function(event){
			event.preventDefault();
			var val = parseInt($(":input.answer:last").data('a'))+1;
			if (isNaN(val))
				val = 0;
			var tmp = "<div class='answer'><label>Answer " + (val+1) + ":</label><br>" +
					"<input type='text' class='answer' data-a='"+val+"'>"+
					"<input type='checkbox' class='right' data-a='2'>"+
					"</div>";
			$('div#control').before(tmp);
		});

		$('button#remove').click(function(event){
			event.preventDefault();
			$('div.answer:last').remove();
		});
	}
);
