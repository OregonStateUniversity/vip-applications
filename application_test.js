/* 
VIP Application Submission
Name: Sabrina Estrada
OSU email: estrab@oregonstate.edu
Description: Testing suite for mapFunc using Jest
*/

const mapFunc = require('./application');

// test to ensure that mapFunc squares the numbers in the array 
test('mapFunc doubles numbers correctly', () => {
    const inputArr = [1, 2, 3, 4];
    const expectedOutput = [1, 4, 9, 16];
    expect(mapFunc(x => x * x, inputArr)).toStrictEqual(expectedOutput);
});

// test to ensure that mapFunc doubles the numbers in the array
test('mapFunc squares numbers correctly', () => {
    const inputArr = [1, 2, 3, 4];
    const expectedOutput = [2, 4, 6, 8];
    expect(mapFunc(x => x * 2, inputArr)).toStrictEqual(expectedOutput);
});

// test to ensure that mapFunc returns an empty array when passed an empty array
test('mapFunc handles empty array correctly', () => {
    const inputArr = [];
    const expectedOutput = [];
    expect(mapFunc(x => x * x, inputArr)).toStrictEqual(expectedOutput);
});
