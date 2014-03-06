$( document ).ready(function() {
        
    $("#departments").change(function(){
        var department_name = $(this).find(":selected").text();
        //alert(department_name);
        var departmentData = {"department": department_name};
        $.ajax({
            url: "getCourses",
            type: "POST",
            data: departmentData,
            dataType: "json",
            success: function(response) {
                $('#courses').empty();
                $('#courses').append($('<option>').text("Select course").attr('value', 'n/a'));
                $.each(response.courses, function(index, value) {
                    $('#courses').append($('<option>').text(value).attr('value', value));
                });
                $('#courses_container').show();
            },
            error: function(response) {
                alert("error");
            }
        });
    });

    $("#courses").change(function(){
        var department_name = $(this).find(":selected").text();
        //alert(department_name);
        var departmentData = {"code": department_name};
        $.ajax({
            url: "getSections",
            type: "POST",
            data: departmentData,
            dataType: "json",
            success: function(response) {
                $('#current_sections').empty();
                $('#desired_sections').empty();
                $('#current_sections').append($('<option>').text("Select current section").attr('value', 'n/a'));
                $('#desired_sections').append($('<option>').text("Select desired section").attr('value', 'n/a'));
                $.each(response.sections, function(index, value) {
                    $('#current_sections').append($('<option>').text(value).attr('value', value));
                    $('#desired_sections').append($('<option>').text(value).attr('value', value));
                });
                $('#current_sections_container').show();
                $('#desired_sections_container').show();
                $('#email').show();
                $('#swap-btn').show();
            },
            error: function(response) {
                alert("error");
            }
        });
    });

});