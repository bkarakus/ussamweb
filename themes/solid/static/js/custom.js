(function($) {

// prettyPhoto
	jQuery(document).ready(function(){
		jQuery('a[data-gal]').each(function() {
			jQuery(this).attr('rel', jQuery(this).data('gal'));
		});  	
		jQuery("a[data-rel^='prettyPhoto']").prettyPhoto({animationSpeed:'slow',theme:'light_square',slideshow:false,overlay_gallery: false,social_tools:false,deeplinking:false});
	});
		
})(jQuery);

(function($) {
	"use strict";
	// isotope 
	var $container = $('.portfolio'),
		$items = $container.find('.portfolio-item'),
		portfolioLayout = 'masonry';
			
	var $grid = $container.isotope({
		itemSelector: '.portfolio-item',
		layoutMode: portfolioLayout,
		resizable: false,
		masonry: { columnWidth: '.grid-sizer' }
	}, refreshWaypoints());
	
	function refreshWaypoints() {
		setTimeout(function() {
		}, 1000);
	}

	$grid.imagesLoaded().progress( function() {
	    $grid.isotope('layout');
	});

	// other stuff
	$('nav.portfolio-filter ul a').on('click', function() {
			var selector = $(this).attr('data-filter');
			$container.isotope({ filter: selector }, refreshWaypoints());
			$('nav.portfolio-filter ul a').removeClass('active');
			$(this).addClass('active');
			return false;
	});

	$("#my-menu").mmenu({
        "navbars": [
            {
               "position": "bottom",
               "content": [
                  "<a class='fa fa-envelope' href='#/'></a>",
                  "<a class='fa fa-twitter' href='#/'></a>",
                  "<a class='fa fa-facebook' href='#/'></a>"
               ]
            }
        ],
        extensions: ["theme-dark", "pagedim-black"],
        offCanvas: {
        	pageSelector: "#wrap-page",
            "position": "right"
        },
	    navbar: {
			title: ""
		},
    });

    var API = $("#my-menu").data("mmenu");

    $("#mymenu-button").click(function() {
        API.open();
    });


	$(window).scroll(navScrolled);
	var flag = true;
	function navScrolled() {
		if ($(window).scrollTop() > 500) {
			if (flag) {
	        	$('.navbar-default').css({
		        	'background': '#2a2f4a',
		        	'top': '-70px',
		        });
		        $('.navbar-default').stop().animate({
		        	'top': '0'
		        }, 500);
		        flag = false;
		    }
	    } else {
       		$('.navbar-default').css({
	       		'background': 'transparent',
	       		'box-shadow': 'none',
	       	});
	       	flag = true;
	    }
	}


	//styling 
	$('.experience .experience-item, #service .service-items:nth-child(2n+2) .service-left, #service .service-items:nth-child(2n+1) .service-right').hover(function() {
		$(this).toggleClass('div-hovered');
	});
})(jQuery);



