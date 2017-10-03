'use strict';

var namesToAges = {
    'Alyssa': 22,
    'Charley': 25,
    'Dan': 25,
    'Jeff': 20,
    'Kasey': 20,
    'Kim': 20,
    'Morgan': 25,
    'Ryan': 25,
    'Stef': 22
};

var ages = Object.values(namesToAges)

function findRarestValue(ages_array) {
    var dict = new Array();
    for (var i = 0; i < ages_array.length; i++) {
        if (ages_array[i] in dict) {
            dict[ages_array[i]] += 1;
        }
        else {
            dict[ages_array[i]] = 1;
        }
    }
    // Grab the key associated with the largest value
    var min_count = Object.keys(dict).reduce(function(a, b){ return dict[a] < dict[b] ? a : b });
    console.log("The rarest age is " + min_count)
    return min_count
}

function findRarestKeys(rarest_age) {
    for (var name in namesToAges) {
        if (namesToAges[name] == rarest_age) {
            console.log(name + " has the rarest age.");
        }
    }
}

// Just testing lodash
var thing = _.filter([1, 2, 3, 4, 5, 6], function (num) {
    return num % 2 === 0;
});

console.log(thing);

var min_age = findRarestValue(ages);
findRarestKeys(min_age);