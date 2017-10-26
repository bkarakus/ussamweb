$(document).ready(function() {
    /* ======= Twitter Bootstrap hover dropdown ======= */
    
    /* Nested Sub-Menus mobile fix */
    
    $('li.dropdown-submenu > a.trigger').on('click', function(e) {
        var current=$(this).next();
		current.toggle();
		e.stopPropagation(); 
		e.preventDefault(); 
		if (current.is(':visible')) {
    		$(this).closest('li.dropdown-submenu').siblings().find('ul.dropdown-menu').hide();
		}
    });
    
    $('a.prettyphoto').prettyPhoto();
    /*
    $('#raporlar-owlcarousel').owlCarousel({
        loop: false,
        margin: 10,
        nav: true,
        dots: false,
        navContainer: '#section-raporlar .owl-nav',
        navText: ["<i class='fa fa-chevron-left'></i>","<i class='fa fa-chevron-right'></i>"],
        responsive: {
            0: {
                items: 1
            },
            600: {
                items: 2
            },
            1000: {
                items: 2
            }
        }
    });
    
    $('#inceleme-gezileri-owlcarousel').owlCarousel({
        loop: false,
        margin: 10,
        nav: true,
        dots: false,
        navContainer: '#section-inceleme-gezileri .owl-nav',
        navText: ["<i class='fa fa-chevron-left'></i>","<i class='fa fa-chevron-right'></i>"],
        responsive: {
            0: {
                items: 1
            },
            600: {
                items: 2
            },
            1000: {
                items: 2
            }
        }
    });
    
    $('#makaleler-owlcarousel').owlCarousel({
        loop: false,
        margin: 10,
        nav: true,
        dots: false,
        navContainer: '#section-makaleler .owl-nav',
        navText: ["<i class='fa fa-chevron-left'></i>","<i class='fa fa-chevron-right'></i>"],
        responsive: {
            0: {
                items: 1
            },
            600: {
                items: 2
            },
            1000: {
                items: 2
            }
        }
    });
    
    $('#kongreler-owlcarousel').owlCarousel({
        loop: false,
        margin: 10,
        nav: true,
        dots: false,
        navContainer: '#section-kongreler .owl-nav',
        navText: ["<i class='fa fa-chevron-left'></i>","<i class='fa fa-chevron-right'></i>"],
        responsive: {
            0: {
                items: 1
            },
            600: {
                items: 2
            },
            1000: {
                items: 2
            }
        }
    });
    
    $('#egitim-owlcarousel').owlCarousel({
        loop: false,
        margin: 10,
        nav: true,
        dots: false,
        navContainer: '#section-egitim .owl-nav',
        navText: ["<i class='fa fa-chevron-left'></i>","<i class='fa fa-chevron-right'></i>"],
        responsive: {
            0: {
                items: 1
            },
            600: {
                items: 2
            },
            1000: {
                items: 2
            }
        }
    });
    
    $('#medya-owlcarousel').owlCarousel({
        loop: false,
        margin: 10,
        nav: true,
        dots: false,
        navContainer: '#section-medya .owl-nav',
        navText: ["<i class='fa fa-chevron-left'></i>","<i class='fa fa-chevron-right'></i>"],
        responsive: {
            0: {
                items: 1
            },
            600: {
                items: 2
            },
            1000: {
                items: 2
            }
        }
    });
    
    $('#haberler-owlcarousel').owlCarousel({
        loop: false,
        margin: 10,
        nav: true,
        dots: false,
        navContainer: '#section-haberler .owl-nav',
        navText: ["<i class='fa fa-chevron-left'></i>","<i class='fa fa-chevron-right'></i>"],
        responsive: {
            0: {
                items: 1
            },
            600: {
                items: 1
            },
            1000: {
                items: 1
            }
        }
    });
    
    $('#saglik-analizleri-owlcarousel').owlCarousel({
        loop: false,
        margin: 10,
        nav: true,
        dots: false,
        navContainer: '#saglik-analizleri .owl-nav',
        navText: ["<i class='fa fa-chevron-left'></i>","<i class='fa fa-chevron-right'></i>"],
        responsive: {
            0: {
                items: 1
            },
            600: {
                items: 1
            },
            1000: {
                items: 1
            }
        }
    });
    
    
*/
});