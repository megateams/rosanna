// datatables
// $(document).ready(function() {
    new DataTable("#table", {
        "aLengthMenu" : [[3,5,10,25,-1],[3,5,10,25,'All']],
        "iDisplayLength": 3
    });
// });

// datatables

// handling sidebar menu click


$('.submenu').css({
    'display' : 'none',
});
$('.main-menu').click(function (e) { 
    e.preventDefault();
    $('.chevron').toggle();

    $('.submenu').toggle();
    
    
});
// handling sidebar menu click



