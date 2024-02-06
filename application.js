/**
 * @param {Function} fn A function to execute for each element in the array
 * @param {Array} arr An array of elements
 * @returns {Array} A new array where each element is the result of the fn
 */
const map = (fn, arr) => {
    const result = []

    for (const elem of arr) {
        result.push(fn(elem))
    }

    return result;
}

module.exports = map;