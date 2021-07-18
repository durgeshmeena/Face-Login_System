
// $("form[name=login_form").submit(function (event) {
//     event.preventDefault();
//     $('#loader1').show();
//     var $form = $(this);
//     var $error = $form.find(".error");


//     var data = $form.serialize() //+ '&imageURI=' + JSON.stringify(imgURI);
//     //console.log(data)

//     $.ajax({
//         url: "/user/login",
//         type: "POST",
//         data: data,
//         dataType: "json",
//         success: function (resp) {
//             $('#loader1').hide();
//             window.location.href = "/dashboard/";
//         },
//         error: function (resp) {
            // $('#loader1').hide();
            // console.log("error= ", resp)
            // $error.text(resp.responseJSON.error).removeClass("error--hidden");
//         }
//     });


// });


<<<<<<< Updated upstream

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
=======
$("form[name=login_form").submit( async(e)=> {
    e.preventDefault();
    $('#loader2').show();
    var $form = $(this);
    var $error = $form.find(".error");


    var form = document.getElementById('myForm2')
    var imgURI = takepicture();
    stopVideo();


    var formData = new FormData(form);
    formData.append("file2", imgURI);

    const res = await fetch('/user/login', {
        method: 'POST',
        body: formData
    });
    const stat = await res.json();    
    console.log(stat)   
    if(stat._id)
    {
        $('#loader2').hide();
        window.location.href = "/dashboard/";
    }
    if(stat.error)
    {
        $('#loader2').hide();
        console.log(stat.error)
        // $error.text(stat.error).removeClass("error--hidden");
        var er = document.getElementById('er2')
        er.innerHTML = stat.error
        er.classList.remove('error--hidden')


    }   


});

>>>>>>> Stashed changes



$("form[name=signup_form").submit( async(e)=> {
    e.preventDefault();
    $('#loader2').show();
    var $form = $(this);
    var $error = $form.find(".error");


    var form = document.getElementById('myForm')
    var imgURI = takepicture();
    stopVideo();

    var formData = new FormData(form);
    formData.append("file", imgURI);

    const res = await fetch('/user/signup', {
        method: 'POST',
        body: formData
    });
    const stat = await res.json();    
    console.log(stat)
    if(stat.sucess)
    {
        $('#loader2').hide();
        window.location.href = "/user/login";
    }    
    if(stat.error)
    {
        $('#loader2').hide();
        var er = document.getElementById('er')
        er.innerHTML = stat.error
        er.classList.remove('error--hidden')
        // $error.text(stat.error).removeClass("error--hidden");
    } 

});


