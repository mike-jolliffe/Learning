var timer;
var interval = 2000;
var clicks = 0;

function showHoles() {
    // Find the available holes
    var holes = [];
    for (var i = 0; i < $('span').length; i++) {
        // Loop through all hole-holding spans and check if image is hole.jpg
        if ($('main').children().eq(i).html() == '<img src="hole.jpg">') {
            holes.push(i);
        }
    }
    return holes;
}

function selectHole() {
    // Select an available hole randomly
    var holesList = showHoles();
    if (holesList.length === 0) {
        alert("You Lose!!");
    }
    return holesList[Math.floor(Math.random() * holesList.length)];
}

function addMole() {
    var hole_for_mole = selectHole();
    console.log(hole_for_mole);
    $('main').children().eq(hole_for_mole).html('<img src="mole.jpg">');
}

$('#start').click(function () {
    timer = setInterval(addMole, interval);
});

$('span').click(function() {
    $(this).html('<img src="hole.jpg">');
    clicks++;
    if (clicks === 10) {
        clicks = 0;
        clearInterval(timer);
        interval -= 500;
        timer = setInterval(addMole, interval);
    }
})
