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
    return holesList[Math.floor(Math.random() * holesList.length)];
}

function addMole() {
    var hole_for_mole = selectHole();
    $('main').children().eq(hole_for_mole).html('<img src="mole.jpg">');
}

function makeMoles() {
    return setInterval(function(){
        addMole()}, 1000);
}

$('#start').click(makeMoles());
$('span').click(this.html('<img src="hole.jpg">'));


