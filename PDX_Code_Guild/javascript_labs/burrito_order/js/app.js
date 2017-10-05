var ingredList = [];
$('.ui.checkbox').checkbox();


// Grab the type of tortilla on click
$('.ui.radio').click(function () {
    if ($('input[type="radio"]').is(':checked')) {
        var ingred = $(this).find('input[value]').val();
        ingredList[0] = '<li>' + ingred + '</li>';
        console.log(ingredList);
        // Put the tortilla type into the aside
        //$('.ingredients.ui.relaxed.list').unshift(ingredList);
        console.log($('#ingredients .ui.relaxed.list').html(ingredList));
    }
});




