// Function definition that takes an array and 
// a customFunction as two parameters. 
// Returns a new array which is the result of 
// applying the customFunction to each element 
// of the original array (i.e., arr). 
export function map(arr, customFunction) {
    let newArr = [];
    arr.forEach(element => {
        newArr.push(customFunction(element));
    });
    return newArr;
}