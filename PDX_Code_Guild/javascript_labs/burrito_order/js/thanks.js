$(function () {

    function getUserInfo () {
        // Parse the document URI to get user's order details
        var uri = document.documentURI;
        var params = uri.split('?')[1];
        params = params.split('&');
        var order_arr = [];
        for (var key_val of params) {
            key_val = key_val.replace(/\+/g, " ");
            key_val = key_val.split('=');
            order_arr.push(key_val)
        }
        return order_arr
    }

    function infoToDict () {
        // Make user order into a dictionary
        var order = getUserInfo();
        order_obj = {};
        for (var item of order) {
            if (order_obj.hasOwnProperty(item[0])) {
                order_obj[item[0]].push(item[1]);
            } else {
                order_obj[item[0]] = [item[1]];
            }
        }
        return order_obj
    }

    function makeHTML () {
        order_dict = infoToDict();
        console.log(order_dict)
        new_dict = {};
        for (var prop in order_dict) {
            var new_val = [];
            for(var val of order_dict[prop]) {
                val = (" ").concat(val);
                new_val.push(val);
            }
            new_dict[prop] = new_val;
        }
        return new_dict
    }

    function toScreen () {
        // Put order details in the browser
        var hidden = ['name', 'credit-card', 'cvv', 'zip', 'terms'];
        var order = makeHTML();
        $('#order-details').empty();
        for (var item in order) {
            if (!(hidden.includes(item))) {
                $('#order-details').append('<span class="userorder"><h4>' + item + ': ' + '</h4>' + '<span>' + order[item] + '</span></span>')
            }
        }
    }
    //  makeHTML()
    toScreen();
});

