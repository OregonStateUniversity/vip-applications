// Author: sycamedia
// Date: 3 December 2023
// Description: For VIP Application. Unit test for application.js using Jest.

// Used this as a guide: https://www.freecodecamp.org/news/how-to-start-unit-testing-javascript/

const map = require("./application");

testArr = [2, -5, 10, 100]

function testFunc(x) {
    return x + 2
}

test("Run map function", () => {
expect(map(testFunc, testArr)).toStrictEqual([4, -3, 12, 102]);
});