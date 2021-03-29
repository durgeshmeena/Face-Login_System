// $('document').ready(function(){


$("form[name=login_form").submit(function (event) {
    event.preventDefault();
    $('#loader1').show();
    var $form = $(this);
    var $error = $form.find(".error");

    //var imgURI = takepicture();
    //stopVideo();
    //console.log('imgURI= ',imgURI);

    var data = $form.serialize() //+ '&imageURI=' + JSON.stringify(imgURI);
    //console.log(data)

    $.ajax({
        url: "/user/login",
        type: "POST",
        data: data,
        dataType: "json",
        success: function (resp) {
            $('#loader1').hide();
            window.location.href = "/dashboard/";
        },
        error: function (resp) {
            $('#loader1').hide();
            console.log("error= ", resp)
            $error.text(resp.responseJSON.error).removeClass("error--hidden");
        }
    });


});




    $("form[name=signup_form").submit(function (e) {
        e.preventDefault();
        $('#loader2').show();
        var $form = $(this);
        var $error = $form.find(".error");
        var data = $form.serialize();
        // console.log("reached here");

        $.ajax({
            url: "/user/signup",
            type: "POST",
            data: data,
            dataType: "json",
            success: function (resp) {
                $('#loader2').hide();
                console.log("sucess");
                window.location.href = '/user/login';
            },
            error: function (resp) {
                $('#loader2').hide();
                console.log("error= ", resp)
                if (resp=="Signup failed"){
                    $error.text(resp.responseJSON.error).removeClass("error--hidden");
                }else{
                    window.location.href = '/user/login';

                }
            }
        });


    });

    // console.log('here1')






// })

