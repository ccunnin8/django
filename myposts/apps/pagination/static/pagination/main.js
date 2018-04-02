var name_field = $("#name");
var from_date_field = $("#from");
var to_date_field = $("#to");
var form = $("form");


name_field.keyup(function(){
  form.submit();
  console.log($(this).val())
});


form.submit(function(e){
  e.preventDefault();
  name = name_field.val()
  from = from_date_field.val()
  to = to_date_field.val()
  $.get("/pagination/search", { name: name, from: from, to: to}).done(function(data){
    render_page(data);
  });
});


function datesComplete(){
  return from_date_field !== "" && to_date_field !== "";
}

from_date_field.on("change",function(){
  if (datesComplete()) {
    form.submit();
  }
})

to_date_field.on("change",function(){
  if (datesComplete()) {
    form.submit();
  }
})

function render_page(data){
  $(".main").html(data);
  add_click_handlers();
}

function add_click_handlers(){
  return $("li a").on("click",function(){
    console.log("CLICKED");
    id = $(this).data("id");
    name = name_field.val()
    from = from_date_field.val()
    to = to_date_field.val()
    $.get("/pagination/search/" + id, { name: name, from: from, to: to}).done(function(data){
      render_page(data);
    });
  })
}
