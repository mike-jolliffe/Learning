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
    total = parseFloat(6 + (0.50 * count) + del_cost).toFixed(2);
    return total;
}

function validateName() {
    // Ensures name field is completed
    var name = $('input[name="name"]').val();
    if (name.split(' ').length === 2) {
        return true;
    } else {
        alert("Please put in your full name")
    }

}

function validateCredit() {
    // Validate the user's credit card number
    var credit = $('input[name="credit-card"]').val().split(' ');
    for (var sub of credit) {
        if ((credit.length == 4) && $.isNumeric(sub)) {
            // Don't do anything
        }
        else {
            alert("Please enter digits in four groups of four");
            return false
        }
    }
    return true
}

function validateCVV() {
    // Validate the CVV number
    var cvv = $('input[name="cvv"]').val();
    if ((cvv.length == 3) && $.isNumeric(cvv)) {
        return true
    } else {
        alert("Please input a three-digit number");
        return false
    }
}

function validateZIP() {
    // Validate the zipcode
    var zip = $('input[name="zip"]').val();
    if ((zip.length == 5) && $.isNumeric(zip)) {
        return true
    } else {
        alert("Please enter a valid 5-digit zipcode");
        return false
    }
}

function validateTerms() {
    if ($('input[name="terms"]').prop('checked')) {
        return true
    } else {
        alert("Please agree to the Terms by checking the box")
    }
}

$('form').click(function () {
    var for_posting = getChecked();
    $('.ui.relaxed.list').empty();
    for (var item of for_posting) {
        $('.ui.relaxed.list').append('<li class="item">' + item + '</li>');
    }

    $('#total_cost').html('<strong>Total:</strong>' + ' $' + priceIt());

});

// On submit, check validate inputs
$('.form').submit(function () {
    if (validateName() &&
        validateCredit() &&
        validateCVV() &&
        validateZIP() &&
        validateTerms()) {
        // Allow page load
        $('.form').append('<input name="total" type="hidden" value=' + "$" + total + '>');
        return true;
    } else {
        return false
    }
});



