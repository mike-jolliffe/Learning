$('#enter').click(function () {
    var new_item = $('#newItem');
    $('#list').append('<li>' + new_item.val() + ' <button class="finished">\t&#10004;</button></li>');
    new_item.val('');

});

$('#list').on('click', '.finished', function () {
    $(this).parent().css('text-decoration', 'line-through');
});

$('#newItem').keypress(function (e) {
    if (e.which === 13) {
        $('#enter').click();
    }
});