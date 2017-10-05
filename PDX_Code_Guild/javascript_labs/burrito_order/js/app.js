var ingredList;
var cleaned;
var total;

$('.ui.checkbox').checkbox();

function getChecked() {
    // Returns the HTML labels associated with all checked boxes
    ingredList = $('form').find('.checkbox');
    var just_html = getHTML();
    return just_html;
}

function getHTML() {
    // Generates a list of only food checkboxes
    cleaned = [];
    for (var item of ingredList) {
        if (($(item).find('input').attr('name') == 'delivery') ||
           ($(item).find('input').attr('name') == 'terms')) {
            // Skip this element
        }
        else if ($(item).find('input').prop('checked') == true) {
            cleaned.push($(item).find('label').html());
        }
    }
    return cleaned;
}

function priceIt() {
    // Calculates the total price of the order, including delivery
    var count = 0;
    var del_cost;
    // Get price of all extra ingredients
    for (var item of ingredList) {
        if ($(item).find('input').prop('checked') == true) {
            if ($(item).find('input').attr('name') == 'extra-ingredients') {
                count += 1;
            }
        }
    }
    if ($('input[value="delivery"]').prop('checked') == true) {
        del_cost = 5;
    } else {
        del_cost = 0;
    }

    // Get price of delivery, if any
    total = 6 + (0.50 * count) + del_cost;
    return parseFloat(total).toFixed(2);
}

function validateName() {
    // Ensures name field is completed
    var name = $('input[name="name"]').val();
    if (name.split(' ').length === 2) {
        return true;
    }
}

function validateCredit() {
    var credit = $('input[name="credit-card"]').val().split(' ');
    for (var sub of credit) {
        if ((credit.length == 4) && $.isNumeric(sub)) {
            // Don't do anything
        }
        else {
            return false
        }
    }
    return true
}

function validateCVV() {
    var cvv = $('input[name="cvv"]').val();
    if ((cvv.length == 3) && $.isNumeric(cvv)) {
        return true
    }
}

function validateZIP() {
    var zip = $('input[name="zip"]').val();
    if ((zip.length == 5) && $.isNumeric(zip)) {
        return true
    }
}

$('form').click(function () {
    var for_posting = getChecked();
    $('.ui.relaxed.list').empty();
    for (var item of for_posting) {
        $('.ui.relaxed.list').append('<li class="item">' + item + '</li>');
    }

    $('#total_cost').html('<strong>Total:</strong>' + ' $' + priceIt());
    //console.log(validateCredit());
    //console.log(validateCVV());
    console.log(validateZIP());
});

// On submit






