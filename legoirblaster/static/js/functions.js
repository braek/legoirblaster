function createSignal(channel, output, speed, brake) {
    $.post('/signals', {
        speed: speed,
        channel: channel,
        output: output,
        brake: brake
    }).done(function(data){
        showCommand(data.command);
    }).fail(function(xhr){
        showError(xhr.responseJSON.error);
    });
}

function showCommand(command) {
    $('#status').html(command).addClass('command').removeClass('error');
}

function showError(error) {
    $('#status').html(error).addClass('error').removeClass('command');
}