"use strict";
//Custom MAP function for VIP

function myMAP(funcParam, arrParam) {
    // This function mimics a MAP function. TWO input parameters: function and 
    // array. One output: array. All index values of the array parameter will 
    // be  passed to the provided function parameter individually and the 
    // return value of that function will then be placed into a result array at 
    // the same index of the original value. The result array will be returned 
    // by myMAP once all indexes of the array parameter have been operated by 
    // the function parameter.

    if (!(typeof funcParam === 'function')) {
        throw new Error("First parameter must be of type function");
    }

    if (!Array.isArray(arrParam)) {
        throw new Error("Second parameter must be of type array");
    }

    let res = [];
    for (let i = 0; i < arrParam.length; i++) {
        res.push(funcParam(arrParam[i]));
    }
    return res
}

module.exports = { myMAP };
