//TODO get default checked fields

var ingredList = [];
$('.ui.checkbox').checkbox();


// Grab the type of tortilla on click
$('.fields:has(label[for="tortilla"]) .ui.radio').change(function () {
    if ($(this).find('input').prop('checked') == true) {
        var ingred = $(this).find('label').html();
        ingredList[0] = ingred;
        console.log(ingredList);
        // Put the tortilla type into the aside
        //$('.ingredients.ui.relaxed.list').unshift(ingredList);
        //console.log($('#ingredients .ui.relaxed.list').html(ingredList));
    }
});

// Grab type of meat and additionals
$('.fields:has(label[for="meat"]) .ui.checkbox').change(function() {
    if ($(this).find('input').prop('checked') == true) {
       // It is not checked, show your div...
       ingredList.push($(this).find('label').html());
   } else if ($(this).find('input').prop('checked') == false) {
       var ingred = $(this).find('label').html();
       var remove_ix = ingredList.indexOf(ingred);
       console.log(remove_ix);
       if (remove_ix > -1) {
           ingredList.splice(remove_ix, 1);
       }
   }
   console.log(ingredList);
});





