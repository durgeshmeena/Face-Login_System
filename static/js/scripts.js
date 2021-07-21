
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


$("form[name=login_form").submit( async(e)=> {
    e.preventDefault();
    $('#loader2').show();

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


$("form[name=login_recog_form").submit( async(e)=> {
    e.preventDefault();
    $('#loader2').show();

    // var form = document.getElementById('myForm3')
    var imgURI = takepicture();
    stopVideo();


    var formData = new FormData();
    formData.append("file3", imgURI);

    const res = await fetch('/user/login-recog', {
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




$("form[name=signup_form").submit( async(e)=> {
    e.preventDefault();
    $('#loader2').show();

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


