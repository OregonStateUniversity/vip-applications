/*
Name: Derrick Macaranas
Github: DerrickMac
Description: VIP Application - Map Function Test Suite
*/

const propMapper = require('./application')

test('propMapper extracts names from objects in an array', () => {
  const arr = [{ name: 'Grace', age: 25 }, { name: 'Kevin', age: 30 }, { name: 'John', age: 21 }]
  const result = ['Grace', 'Kevin', 'John']

  const getProp = (obj, prop) => obj[prop]

  expect(propMapper(getProp, arr, 'name')).toEqual(result)
})

test('propMapper extracts ages from objects in an array', () => {
  const arr = [{ name: 'Grace', age: 25 }, { name: 'Kevin', age: 30 }, { name: 'John', age: 21 }]
  const result = [25, 30, 21]

  const getProp = (obj, prop) => obj[prop]

  expect(propMapper(getProp, arr, 'age')).toEqual(result)
})
