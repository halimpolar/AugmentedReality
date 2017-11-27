
$(function(){
    $('#fileupload').fileupload({
        url: 'upload',
        dataType: 'json',
        add: function(e, data) {
            data.submit();
        },
        success: function(response, status) {
            console.log(response.filename);
            var filePath = 'static/Uploads/' + response.filename;
            //$('#imgUpload').attr('src',filePath);
            console.log('success');
        },
        error: function(error) {
            console.log(error);
        }
    });

	$('#btnSignUp').click(function(){
		
		$.ajax({
			url: '/signUp',
			data: $('form').serialize(),
            type: 'POST',
			success: function(response){
				console.log(response);
				if (response) {
					top.location.href = "../dashboard";
				}
			},
			error: function(error){
				console.log(error);
			}
		});
	});
});