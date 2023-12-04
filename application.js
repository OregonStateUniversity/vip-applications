// Author: sycamedia
// Date: 3 December 2023
// Description: For VIP Application. Defines a 'map' function in JavaScript.

/**
 * 
 * @param {Object} func The function to apply to array items
 * @param {Object} arr An array of values
 * @returns An array with the mapped values
 */
 function map(func, arr) {
    result = []
    for (let i = 0; i < arr.length; i++) {
        result.push(func(arr[i]))
    }
    return result
}