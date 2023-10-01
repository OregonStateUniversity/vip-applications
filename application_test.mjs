// Import the map function
import { map } from './application.mjs'

// Simple unit test for the map function
const inputArr = [4, 9, 16, 25];
const resultArr = map(inputArr, Math.sqrt);
if (JSON.stringify(resultArr) === JSON.stringify([2, 3, 4, 5])) {
    console.log("The test has been passed!");
} else {
    console.log("Test is not passed.");
}
