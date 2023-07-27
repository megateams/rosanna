
// datatables
// $(document).ready(function() {
    new DataTable("#table", {
        // responsive: true,
        // scrollX: true,
        "aLengthMenu" : [[3,5,10,25,-1],[3,5,10,25,'All']],
        "iDisplayLength": 3,
        
    });
// });

// datatables

// handling sidebar menu click


$('.submenu').css({
    'display' : 'none',
});
$('.submenu1').css({
    'display' : 'none',
});
$('.submenu2').css({
    'display' : 'none',
});
$('.submenu-acc').css({
    'display' : 'none',
});
$('.submenu-acad').css({
    'display' : 'none',
});
$('.submenu-users').css({
    'display' : 'none',
});


$('.main-menu').click(function (e) { 
    e.preventDefault();
    $('.chevron').toggle();

    $('.submenu').toggle(); 
});
$('.main-menu-staff').click(function (e) { 
    e.preventDefault();
    $('.chevron0').toggle();

    $('.submenu-staff').toggle();
});
$('.main-submenu1').click(function (e) { 
    e.preventDefault();
    $('.chevron1').toggle();

    $('.submenu1').toggle();
});
$('.main-submenu2').click(function (e) { 
    e.preventDefault();
    $('.chevron2').toggle();

    $('.submenu2').toggle();
});
$('.main-menu-acc').click(function (e) { 
    e.preventDefault();
    $('.chevron-acc').toggle();

    $('.submenu-acc').toggle();
});
$('.main-menu-acad').click(function (e) { 
    e.preventDefault();
    $('.chevron-acad').toggle();

    $('.submenu-acad').toggle();
});
$('.main-menu-users').click(function (e) { 
    e.preventDefault();
    $('.chevron-users').toggle();

    $('.submenu-users').toggle();
});
// handling sidebar menu click
$(".guardian").hide();
$(".livingwith").change(function (e) { 
    e.preventDefault();
    
    let optionValue = document.querySelector(".livingwith").value;

    if(optionValue === "Guardian"){
        $(".guardian").show();
    }
    else
    {
        $(".guardian").hide();
    }

});

// more student details
// $(document).ready(function () {
    $(document).ready(function() {
        $('.more').click(function(e) {
            e.preventDefault();
            $(".table-section").hide();
            var studentId = $(this).attr('id');
            alert(studentId);
            $.ajax({
                url: '/showstudent',  // Replace with the appropriate URL
                type: 'POST',
                data: { studentId: studentId },
                success: function(response) {
                    $('.show_student').html(response);
                },
                error: function(xhr) {
                    // Handle error case
                    console.log(xhr.responseText);
                }
            });
        });
        
        // support staff details
        $('.more_support_staff').click(function(e) {
            e.preventDefault();
            $(".table-section").hide();
            var staffId = $(this).attr('id');
            alert(staffId);
            $.ajax({
                url: '/show-support-staff',  // Replace with the appropriate URL
                type: 'GET',
                data: { staffId: staffId },
                success: function(response) {
                    $('.show_support_staff').html(response);
                },
                error: function(xhr) {
                    // Handle error case
                    console.log(xhr.responseText);
                }
            });
        });
    });
    
// });



