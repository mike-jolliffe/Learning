"use strict";

var animalNoises = {
    name: null,
    age: 0,
    makeDogNoise: function () {
        return 'Woof';
    },
    makeCatNoise: function () {
        return "Meow"
    }
};

$('.body').click(function(){
    $(this).children().eq(1).css({"background-color": "yellow"});
});


// console.log(animalNoises.makeCatNoise());
// console.log(animalNoises.makeDogNoise());
