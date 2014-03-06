$( document ).ready(function() {
        
    $("#departments").change(function(){
        var id = $(this).find(":selected").text();
        alert(id);
    });


      /*  var frm = $('#departments');
        frm.submit(function () {
            $.ajax({
                type: frm.attr('method'),
                url: frm.attr('action'),
                data: frm.serialize(),
                success: function (data) {
                    alert("Yes")
                },
                error: function(data) {
                    alert("no")
                }
            });
            return false;
        }); */

});