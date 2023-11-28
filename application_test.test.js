
/*Unit testing with jest*/

// To test locally have npm installed
// Run "npm install --save-dev jest" in terminal
// Run "npm install --save-dev @jest/globals" in terminal 
// Configure package.json:
/*
{
    "devDependencies": {
        "@jest/globals": "^29.7.0",
        "jest": "^29.7.0"
    },
    "scripts": {
        "test": "jest"
    }

}

*/
// Finally run "npm test" in terminal

"use strict";
const { describe, expect, test } = require('@jest/globals');
const { myMAP }  = require('./application.js');


describe('myMAP function', () => {
    test('should add 5 to each element of the array', () => {
        const result = myMAP(a => a + 5, [1, 2, 3]);
        expect(result).toEqual([6, 7, 8]);
    });

    test('should return an empty array', () => {
        const result = myMAP(a => a * 2, []);
        expect(result).toEqual([]);
    });

    test('should throw an error if the first parameter is not a function', () => {
        expect(() => 
            myMAP('not a function', [1, 2, 3])).toThrow('First parameter must be of type function');
    });

    test('should throw an error if the second parameter is not an array', () => {
        expect(() => 
            myMAP(a => a + 5, 'not an array')).toThrow('Second parameter must be of type array');
    });

});

