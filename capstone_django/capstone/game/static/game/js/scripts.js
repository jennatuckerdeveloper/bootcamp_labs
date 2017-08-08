$('#gameplay').bind("enterKey",function(e){
   e.preventDefault();

   $.ajax({
       type: 'POST',
       url: '/game/gameplay_entry/',
       data: {
           choice: $('#gameplay').val()
    },
       success:function(data){
           console.log(data);
           window.location.href = "/game/names/";
       }
   })
});
$('#gameplay').keyup(function(e){
    if(e.keyCode == 13)
    {
        $(this).trigger("enterKey");
    }
});
//
// $('#name5').bind("enterKey",function(e){
//    e.preventDefault();
//
//    $.ajax({
//        type: 'POST',
//        url: '/game/gameplay_entry/',
//        data: {
//            choice2: $('#name2').val(),
//            choice3: $('#name3').val(),
//            choice4: $('#name4').val(),
//            choice5: $('#name5').val()
//     },
//        success:function(data){
//            console.log(data);
//            // window.location.href = "/game/packing/";
//        }
//    })
// });
// $('#name5').keyup(function(e){
//     if(e.keyCode == 13)
//     {
//         $(this).trigger("enterKey");
//     }
// });

$( "#names" ).click(function() {

   $.ajax({
       type: 'POST',
       url: '/game/names_entry/',
       data: {
           choice2: $('#name2').val(),
           choice3: $('#name3').val(),
           choice4: $('#name4').val(),
           choice5: $('#name5').val()
    },
       success:function(data){
           console.log(data);
           window.location.href = "/game/packing/";
       }
   })
});

// There may be a way to do this systematically for name2, name3, name4.

$('#pack').bind("enterKey",function(e){
   e.preventDefault();

   $.ajax({
       type: 'POST',
       url: '/game/packing_entry/',
       data: {
           choice: $('#pack').val()
    },
       success:function(data){
           console.log(data);

       }
   })
});
$('#pack').keyup(function(e){
    if(e.keyCode == 13)
    {
        $(this).trigger("enterKey");
    }
});

$( "#done" ).click(function() {
  window.location.href = "/game/depart/";
});

$('#unpack').bind("enterKey",function(e){
   e.preventDefault();

   $.ajax({
       type: 'POST',
       url: '/game/gameplay_entry/',
       data: {
           choice: $('#unpack').val()
    },
       success:function(data){
           console.log(data);
       }
   })
});
$('#unpack').keyup(function(e){
    if(e.keyCode == 13)
    {
        $(this).trigger("enterKey");
    }
});

$( "#gotopack" ).click(function() {
  window.location.href = "/game/packing/";
});

$( "#depart" ).click(function() {
  window.location.href = "/game/play/";
});

$('#play').bind("enterKey",function(e){
   e.preventDefault();

   $.ajax({
       type: 'POST',
       url: '/game/play_entry/',
       data: {
           move: $('#play').val()
    },
       success:function(data){
           console.log(data);
       }
   })
});
$('#play').keyup(function(e){
    if(e.keyCode == 13)
    {
        $(this).trigger("enterKey");
    }
});