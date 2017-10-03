"use strict";

function sortNumber(a, b) {
    // makes a compareFunction to be given to sort
    return a - b;
}

function median(data) {
    // Sorts an array of integers using compareFunction, then returns the median
    data = data.sort(sortNumber);
    var strLen = data.length;
    var half = Math.floor(strLen / 2)
    if (strLen % 2 === 0) {
        console.log((data[half - 1] + data[half]) / 2)
        return (data[half - 1] + data[half]) / 2
    } else {
        console.log(data[half])
        return data[half]
    }
}


median([1, 2, 3, 4, 5]);  // 3
median([3, 1, 2, 5, 3]);  // 3
median([1, 300, 2, 200, 1]);  // 2
median([3, 6, 20, 99, 10, 15]);  // 12.5
