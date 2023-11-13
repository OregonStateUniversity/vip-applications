/*
Name: Derrick Macaranas
Github: DerrickMac
Description: VIP Application - Custom Map Function
*/

function propMapper (func, arr, prop) {
  const result = []

  for (let i = 0; i < arr.length; i++) {
    result[i] = func(arr[i], prop)
  }

  return result
}

module.exports = propMapper
