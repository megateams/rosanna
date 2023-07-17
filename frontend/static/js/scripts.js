// handling sidebar menu click


$('.submenu').css({
    'display' : 'none',
})
$('.main-menu').click(function (e) { 
    e.preventDefault();
    $('.chevron').toggle();

    $('.submenu').toggle();
    
    
});
// handling sidebar menu click

