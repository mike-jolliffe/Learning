

function transform(input) {
  if (input) {
    clearError();
    // Calculate the number of quarters necessary first.
    var running_amt = parseInt(input);

    var numQ = Math.floor(running_amt / 25);
    running_amt = running_amt % 25;

    // Calculate the number of dimes
    var numD = Math.floor(running_amt / 10);
    running_amt = running_amt % 10;

    // Number of nickles
    var numN = Math.floor(running_amt / 5);
    running_amt = running_amt % 5;

    // Number of pennies
    var numP = Math.floor(running_amt / 1);

    // Return minimum number of coins for user
    var result = String(numQ + numD + numN + numP);
    printResult(result + " coins: " + numQ + " quarters, " + numD + " dimes, "
                + numN + " nickles, and " + numP + " pennies");
  }
  else {
    printError('Enter a value');
    focusInput();
  }
}

document.addEventListener('DOMContentLoaded', function (evt) {

  setup(transform);
  focusInput();
});


function focusInput() {
  document.querySelector('[name="input"]').focus();
}

function printResult(str) {
  $('#result').html(str);
}

function printError(str) {
  var err = document.getElementById('error');
  err.classList.add('error');
  err.innerHTML = str;
}

function clearError() {
  var err = document.getElementById('error');
  err.innerHTML = '';
  err.classList.remove('error');
}

function setup(callback) {
  document.querySelector('form')
    .addEventListener('submit', function (evt) {
    evt.preventDefault();
    var value = document.querySelector('input').value;
    callback(value);
  });
}
