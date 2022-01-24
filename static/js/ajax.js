$('.btn-submit').on('click', function() {
    $body.addClass('modal_in');
    $modalWrap.fadeIn(300);
    $body.css('padding-right', getScrollWidth());
    formSubmit();
});

function formSubmit() {
    console.log("function formSubmit()");
    var params = $("#formPetition").serialize();
    console.log(params);
    $.ajax({
        url: '/api/check_validation',
        type: 'POST',
        data: params,
        contentType: 'application/x-www-form-urlencoded; charset=UTF-8',
        dataType: 'html',
        success: function(data) {
            data = JSON.parse(data)
            console.log(data);
            console.log(data.content_1.prediction);
            console.log(data.content_2.prediction);
            console.log(data.content_7.prediction);
        }
    });
}