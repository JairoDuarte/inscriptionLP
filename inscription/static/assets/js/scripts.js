
function scroll_to_class(element_class, removed_height) {
	var scroll_to = $(element_class).offset().top - removed_height;
	if($(window).scrollTop() != scroll_to) {
		$('html, body').stop().animate({scrollTop: scroll_to}, 0);
	}
}

function bar_progress(progress_line_object, direction) {
	var number_of_steps = progress_line_object.data('number-of-steps');
	var now_value = progress_line_object.data('now-value');
	var new_value = 0;
	if(direction == 'right') {
		new_value = now_value + ( 100 / number_of_steps );
	}
	else if(direction == 'left') {
		new_value = now_value - ( 100 / number_of_steps );
	}
	progress_line_object.attr('style', 'width: ' + new_value + '%;').data('now-value', new_value);
}

function validateForm() {
	$("#_errors").html('<b>veillez saisir les champs s\'il vous plaît, tous les champs sont obligataires.</b>');

	console.log('teste');
	jQuery(document).ready(function() {
		var parent_fieldset = $(this).parents('fieldset');
    	var next_step = true;
    	// navigation steps / progress steps
    	var current_active_step = $(this).parents('.f1').find('.f1-step.active');
    	var progress_line = $(this).parents('.f1').find('.f1-progress-line');

    	// fields validation
    	parent_fieldset.find('input[type="text"],input[type="number"], input[type="password"], textarea').each(function() {
    		if( $(this).val() == "" ) {
    			$(this).addClass('input-error');
    			$("#_errors").html('<b>veillez saisir les champs s\'il vous plaît, tous les champs sont obligataires.</b>');
				next_step = false;
				return false;
    		}
    		else {
    			$("#_errors").html('')
    			$(this).removeClass('input-error');
    		}
    	});

    });
}

function Validat(parent_fieldset) {
	var inu=0, itx=0;
	$("#_errors").html('')
	var next_step = true;
	parent_fieldset.find('input[type="text"],input[type="number"],input[type="password"], textarea').each(function() {
    		if( $(this).val() == "" ) {

    			if ($(this).attr('type') !='number' && inu ==0) {
    				inu++;
                    $("#_errors").html($("#_errors").html() + ' <b>veillez saisir les champs s\'il vous plaît, tous les champs sont obligataires.</b> ');
                }
    			else if(itx==0) {
    				itx++;
    				x =$(this).val();//   document.getElementById("numb").value;

					// If x is Not a Number or less than one or greater than 10
					if (isNaN(x) || x < 0 || x > 20) {
						text = "Input not valid";
					} else {
						text = "Input OK";
					}
    				$("#_errors").html($("#_errors").html()+'<b>  veillez saisir les champs s\'il vous plaît, tous les champs sont obligataires 0-20.</b> ');
				}
    			$(this).addClass('input-error');
				next_step = false;
    		}
    		else {
    			//$("#_errors").html('')
    			$(this).removeClass('input-error');
    		}
    	});

	return next_step;
}

jQuery(document).ready(function() {


    /*
        Fullscreen background
    */
    $.backstretch("assets/img/backgrounds/1.jpg");
    
    $('#top-navbar-1').on('shown.bs.collapse', function(){
    	$.backstretch("resize");
    });
    $('#top-navbar-1').on('hidden.bs.collapse', function(){
    	$.backstretch("resize");
    });
    
    /*
        Form
    */
    $('.f1 fieldset:first').fadeIn('slow');
    
    $('.f1 input[type="text"], .f1 input[type="password"], .f1 textarea').on('focus', function() {
    	$(this).removeClass('input-error');
    });

    // next step
    $('.f1 .btn-next').on('click', function() {
    	var inu=0, itx=0;
    	$("#_errors").html('')
    	var parent_fieldset = $(this).parents('fieldset');
    	var next_step = true;
    	// navigation steps / progress steps
    	var current_active_step = $(this).parents('.f1').find('.f1-step.active');
    	var progress_line = $(this).parents('.f1').find('.f1-progress-line');
    	
    	// fields validation
    	// fields validation
		next_step =  Validat(parent_fieldset);
    	
    	if( next_step ) {
    		$("#_errors").html('');
    		parent_fieldset.fadeOut(400, function() {
    			// change icons
    			current_active_step.removeClass('active').addClass('activated').next().addClass('active');
    			// progress bar
    			bar_progress(progress_line, 'right');
    			// show next step
	    		$(this).next().fadeIn();
	    		// scroll window to beginning of the form
    			scroll_to_class( $('.f1'), 20 );
	    	});
    	}
    	
    });
    
    // previous step
    $('.f1 .btn-previous').on('click', function() {
    	// navigation steps / progress steps
    	var current_active_step = $(this).parents('.f1').find('.f1-step.active');
    	var progress_line = $(this).parents('.f1').find('.f1-progress-line');
    	
    	$(this).parents('fieldset').fadeOut(400, function() {
    		// change icons
    		current_active_step.removeClass('active').prev().removeClass('activated').addClass('active');
    		// progress bar
    		bar_progress(progress_line, 'left');
    		// show previous step
    		$(this).prev().fadeIn();
    		// scroll window to beginning of the form
			scroll_to_class( $('.f1'), 20 );
    	});
    });
    
    // submit
    $('.f1 .btn-submit').on('click', function(e) {
    	
    	// fields validation
    	$(this).find('input[type="text"], input[type="password"], textarea').each(function() {
    		if( $(this).val() == "" ) {
    			//e.preventDefault();
    			$(this).addClass('input-error');
    			$("#_errors").html('<b>veillez saisir les champs s\'il vous plaît, tous les champs sont obligataires.</b>');

    		}
    		else {
    			$(this).removeClass('input-error');
    		}
    	});
    	// fields validation
    	
    });


    
    
});
