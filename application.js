/* 
VIP Application Submission
Name: Sabrina Estrada
OSU email: estrab@oregonstate.edu
Description: Custom map function implementation 
*/

function mapFunc(func, arr) {
    let newArr = []

    for (let i = 0; i < arr.length; i++) {
        newArr[i] = func(arr[i]);
    }
    return newArr;
}

module.exports = mapFunc;