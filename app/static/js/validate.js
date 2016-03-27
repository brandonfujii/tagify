var $imageForm = $('#imageform'),
$resultImage = $('.results .image img'),
$results = $('.results'),
$clearForm = $('#clear'),
$mainInput = $('#imageurl');


$(document).ready(function() {
	if ($resultImage.attr('src')) {
		$results.addClass('active');
	} else {
		$results.removeClass('active');
	}

});

$clearForm.on('click', function(e) {
	e.preventDefault();
	$mainInput.val('');
});


