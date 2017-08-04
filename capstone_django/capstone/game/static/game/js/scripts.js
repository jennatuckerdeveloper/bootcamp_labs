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

$('#name2').bind("enterKey",function(e){
   e.preventDefault();

   $.ajax({
       type: 'POST',
       url: '/game/gameplay_entry/',
       data: {
           choice: $('#name2').val()
    },
       success:function(data){
           console.log(data);

       }
   })
});
$('#name2').keyup(function(e){
    if(e.keyCode == 13)
    {
        $(this).trigger("enterKey");
    }
});

$('#name3').bind("enterKey",function(e){
   e.preventDefault();

   $.ajax({
       type: 'POST',
       url: '/game/gameplay_entry/',
       data: {
           choice: $('#name3').val()
    },
       success:function(data){
           console.log(data);

       }
   })
});
$('#name3').keyup(function(e){
    if(e.keyCode == 13)
    {
        $(this).trigger("enterKey");
    }
});

$('#name4').bind("enterKey",function(e){
   e.preventDefault();

   $.ajax({
       type: 'POST',
       url: '/game/gameplay_entry/',
       data: {
           choice: $('#name4').val()
    },
       success:function(data){
           console.log(data);

       }
   })
});
$('#name4').keyup(function(e){
    if(e.keyCode == 13)
    {
        $(this).trigger("enterKey");
    }
});

$('#name5').bind("enterKey",function(e){
   e.preventDefault();

   $.ajax({
       type: 'POST',
       url: '/game/gameplay_entry/',
       data: {
           choice: $('#name5').val()
    },
       success:function(data){
           console.log(data);
           window.location.href = "/game/packing/";
       }
   })
});
$('#name5').keyup(function(e){
    if(e.keyCode == 13)
    {
        $(this).trigger("enterKey");
    }
});

// There may be a way to do this systematically for name2, name3, name4.

$('#pack').bind("enterKey",function(e){
   e.preventDefault();

   $.ajax({
       type: 'POST',
       url: '/game/gameplay_entry/',
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

