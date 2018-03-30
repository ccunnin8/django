function delete_note(){
  $("#delete").on("click",function(e){
    e.preventDefault();
    $.ajax({
      url: $(this).attr("href"),
      method: "GET",
      success: function(){
        $(this).parent().remove();
      },
      error: function(){
        console.log("error removing");
      }
    });
  });
};

function update_note(){
  $("textarea").on("keyup",function(){
    $.ajax({
      url: $(this).parent().attr("action"),
      method: "POST",
      data: $(this).parent().serialize(),
      success: function(){
        console.log("updated successfully")
      }
    })
  })
};

function add_note(){
  $("#add_note").submit(function(e){
    e.preventDefault();
    $.ajax({
      url: $(this).attr("action"),
      method: "POST",
      data: $(this).serialize(),
      success: function(data){
        append_note(data)
      }
    });
  });
};

function append_note(data){
  $(".notes").append(data);
  delete_note();
  update_note();
};

add_note();
delete_note();
update_note();
