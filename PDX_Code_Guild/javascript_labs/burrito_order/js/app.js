var ingredList = [];
$('.ui.checkbox').checkbox();


// Grab the type of tortilla on click
$('.ui.radio').click(function () {
    if ($('input[name="tortilla"]').is(':checked')) {
        var ingred = $(this).find('input[value]').val();
        ingredList[0] = '<li>' + ingred + '</li>';
        console.log(ingredList);
        // Put the tortilla type into the aside
        //$('.ingredients.ui.relaxed.list').unshift(ingredList);
        //console.log($('#ingredients .ui.relaxed.list').html(ingredList));
    }
});

// Grab type of meat and additionals
$('.ui.checkbox').change(function() {
    if ($(this).find('input').prop('checked') == true) {
       // It is not checked, show your div...
       ingredList.push($(this).find('label').html());
   } else if ($(this).find('input').prop('checked') == false) {
       var ingred = $(this).find('label').html();
       var remove_ix = ingredList.indexOf('<li>' + ingred + '</li>');
       console.log(remove_ix);
       ingredList.splice(remove_ix);
   }
   console.log(ingredList);
});

// $('.ui.checkbox').click(function () {
//     if ($('input[name="meat"]').is(':checked')) {
//         var ingred = $(this).find('input[value]').val();
//         ingredList.push('<li>' + ingred + '</li>');
//     } else if ($('input[type="checkbox"]').is(':not(:checked)')) {
//         var ingred = $(this).find('input[value]').val();
//         console.log(ingred);
//         var remove_ix = ingredList.indexOf('<li>' + ingred + '</li>');
//         console.log(remove_ix);
//         ingredList.splice(remove_ix);
//     }
//     console.log(ingredList);
// });




