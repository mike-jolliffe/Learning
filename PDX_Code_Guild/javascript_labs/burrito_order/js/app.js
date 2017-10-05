//TODO get default checked fields

var ingredList;

function getChecked() {
    ingredList = $('form').find('.checkbox');
    var just_html = getHTML();
    return just_html;
}

function getHTML() {
    var cleaned = [];
    for (var item of ingredList) {
        if ($(item).find('input').attr('name') == 'delivery') {
            // Skip this element
        }
        else if ($(item).find('input').prop('checked') == true) {
            cleaned.push($(item).find('label').html());
        }
    }
    return cleaned;
}
$('.ui.checkbox').checkbox();
console.log(getChecked());


// Grab the type of tortilla on click
// $('.fields:has(label[for="tortilla"]) .ui.radio').change(function () {
//     if ($(this).find('input').prop('checked') == true) {
//         var ingred = $(this).find('label').html();
//         ingredList[0] = ingred;
//         console.log(ingredList);
//         // Put the tortilla type into the aside
//         //$('.ingredients.ui.relaxed.list').unshift(ingredList);
//         //console.log($('#ingredients .ui.relaxed.list').html(ingredList));
//     }
// });

// Grab type of meat and additionals
// $('.fields:has(label[for="meat"]) .ui.checkbox').change(function() {
//     if ($(this).find('input').prop('checked') == true) {
//        // It is not checked, show your div...
//        ingredList.push($(this).find('label').html());
//    } else if ($(this).find('input').prop('checked') == false) {
//        var ingred = $(this).find('label').html();
//        var remove_ix = ingredList.indexOf(ingred);
//        console.log(remove_ix);
//        if (remove_ix > -1) {
//            ingredList.splice(remove_ix, 1);
//        }
//    }
//    console.log(ingredList);
// });

$('form').click(function () {
    var for_posting = getChecked();
    $('.ui.relaxed.list').empty();
    for (var item of for_posting) {
        $('.ui.relaxed.list').append('<li class="item">' + item + '</li>');
    }
});

// Keep everything above "Your Details" out of ingred list
// Count number of extra ingredients
// Add to the cost




