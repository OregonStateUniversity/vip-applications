const map = require('./application');

it('should call the function for each element', () => {
    const multiply = jest.fn();

    map(multiply, [1, 2, 3]);

    expect(multiply).toHaveBeenCalledTimes(3);
});

it('should not mutate the passed array', () => {
    const numbers = [1, 2, 3];

    map((el) => el + 1, numbers);

    expect(numbers).toEqual([1, 2, 3]);
});

it('should execute the passed function on every element in the array', () => {
    expect(map((el) => el ** 2, [1, 2, 3])).toEqual([1, 4, 9]);
});

it('should do nothing if the array is empty', () => {
    expect(map((el) => el ** 2, [])).toEqual([]);
});
