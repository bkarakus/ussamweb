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
});