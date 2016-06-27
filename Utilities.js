/**
 * Created by Trinity on 27/06/2016.
 */
"use strict";

export function jsonify(string) {
    return "[" + string.replace(/\n/g ,",") + "]";
}

export function insertionSort(array,key) {
    let value,j;
    for (let i = 0; i < array.length; i++) {
        value = array[i];
        j = i - 1;
        while( j >= 0 && array[j][key] > value[key]) {
            array[j+1] = array[j];
            j--;
        }
        array[j+1] = value;
    }
    return array;
}