"use strict";

function isUnique(arr, el) {
    var hasOne = false;
    for (let item of arr) {
        if (item === el) {
            if (hasOne) {
                return false;
            } else {
                hasOne = true;
            }
        }
    }
    return true;
}

function nonUniqueElements(data) {
    const new_array = [];
    for (let item of data) {
        if (!isUnique(data, item)) {
            new_array.push(item);
        }
    }
    console.log(data, new_array);
    return new_array;
}



nonUniqueElements([1, 2, 3, 1, 3]);  // [1, 3, 1, 3]
nonUniqueElements([1, 2, 3, 4, 5]);  // []
nonUniqueElements([5, 5, 5, 5, 5]);  // [5, 5, 5, 5, 5]
nonUniqueElements([10, 9, 10, 10, 9, 8]);  // [10, 9, 10, 10, 9]


