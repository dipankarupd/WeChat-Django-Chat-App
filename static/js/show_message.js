$(document).ready(()=> {

    let roomname = $('#card').data('roomname')
    setInterval(()=> {
        $.ajax({
            type: 'GET',
            url: '/get/' + roomname,

            success: (response)=> {
                console.log(response);
    
                $('#chat-container').empty()
    
                for(var key in response.message) {
                    temp = '<div class="chats"><b>'+response.message[key].username+'</b><p>'+response.message[key].message+'</p> <h5>'+response.message[key].time+'</h5></div>'
                    $('#chat-container').append(temp)
                }
            },
            error: (response)=> {
                alert("Error occured")
            }
        })
    },1000)
})