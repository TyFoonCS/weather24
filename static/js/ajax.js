$( document ).ready(function() {
    $("#btn-floating waves-effect waves-light red").click(
		function(){
			sendAjaxForm('result_form', 'ajax_form', 'http://127.0.0.1:5000/', 1);
			return false;
		}
	);
});

function sendAjaxForm(result_form, ajax_form, url, mark) {
    $.ajax({
        mark: mark
        url:     url, //url страницы (action_ajax_form.php)
        type:     "POST", //метод отправки
        dataType: "html", //формат данных
        data: $("#"+ajax_form).serialize(),  // Сеарилизуем объект
        success: function(response) { //Данные отправлены успешно
        	result = $.parseJSON(response);
        	$('#result_form').html(result);
    	},
    	error: function(response) { // Данные не отправлены
            $('#result_form').html('Ошибка. Данные не отправлены.');
    	}
 	});
}