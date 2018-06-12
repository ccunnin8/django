$(document).ready(function(){
  $(".icon").click(function(){
    $(".sidebar").toggle("slow");
  });

  $(".sidebar form").submit(function(e){
    e.preventDefault();
    var data = $(this).serialize();
    $.ajax({
      type: "POST",
      url: "/settings/",
      data: data,
      success: function(data){
          console.log(data);
          $(".sidebar").toggle("slow");
      },
    }).fail(function(){
      console.log("failed");
    })
  });
});
