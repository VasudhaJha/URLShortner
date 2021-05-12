$("#copy").hide()

function send() {
    var url = {
        long_url: $("#text_field").val(),
    }

    $.ajax({
        url: '/',
        type: 'post',
        dataType: 'json',
        contentType: 'application/json',
        data: JSON.stringify(url),
        success: function (response) {
            $("#ok").hide()
            console.log(response);
            $("#text_field").val(response["short_url"])
            $("#copy").show()
        }
    });
}

function copy() {
    $("#text_field").select()
    document.execCommand("copy");
}
