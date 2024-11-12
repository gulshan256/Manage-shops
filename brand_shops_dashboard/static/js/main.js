$(document).ready(function() {

	$("body").tooltip({ selector: '[data-bs-toggle=tooltip]' });

	$(".auto_close_alert").fadeTo(2000, 500).slideUp(500, function(){
		$(this).slideUp(2000);
	});


});