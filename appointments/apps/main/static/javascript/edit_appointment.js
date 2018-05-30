$(document).ready(function(){
  $(".edit").click(function(){
    var id = $(this).data("id");
    //click on the same one switch the form back to ADD
    if (parseInt($("input[name='appointment_id']").val()) === id){
      toggle_forms()
    }
    else{
      $.get("/appointments/edit/" + id, function(data){
          //didnt click on the same one so check if going from add->edit or edit->edit
          if ($("#edit_form").parent().hasClass("is-hidden")){
            toggle_forms();
          }
          //change fields in edit form to represent data
          populate_form_data(data);
        });
    }
  });

  $("#cancel").click(function(e){
    e.preventDefault();
    toggle_forms();
  });

  function toggle_forms(){
      var add_form = $(".card:first-child")
      var edit_form = add_form.next();
      if (!add_form.hasClass("is-hidden")){
        add_form.addClass("is-hidden");
        edit_form.removeClass("is-hidden");
      }
      else {
        add_form.removeClass("is-hidden");
        edit_form.addClass("is-hidden");
      }
  };

  function populate_form_data(data){
    var edit_form = $("#edit_form")
    edit_form.find("select[name='date_day']").val(data.day);
    edit_form.find("select[name='date_month']").val(data.month);
    edit_form.find("select[name='date_year']").val(data.year);
    edit_form.find("select[name='hour']").val(data.hour);
    edit_form.find("select[name='minute']").val(data.minute);
    edit_form.find("select[name='am_or_pm']").val(data.am_or_pm);
    edit_form.find("input[name='tasks']").val(data.tasks);
    edit_form.find("input[name='appointment_id']").val(data.id);
  };


});
