
$("form").submit(function(e){
  e.preventDefault();
  $.ajax({
    url: "/add_post",
    method: "POST",
    data: $(this).serialize(),
    success: function(data){
      updatePage(data);
    }
  });
});


function updatePage(data){
  $(".posts").append(data);
}
