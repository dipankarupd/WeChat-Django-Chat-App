$(document).on('submit', '#post-form', (event)=> {

    event.preventDefault()

    $.ajax({
        type: 'POST',
        url: '/send',
        data: {
            username: $('#username').val(),
            room_id: $('#room_id').val(),
            message: $('#txt').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),

        },

        success: (data) => {
            // alert(data)
        }
    });

    document.getElementById('message').value = ''
});