def add_ten(number):
    return number + 10

numbers = [823, 543, 32, 900, 10, 42, 9.99, 54.87]

ten_percent_numbers = map(add_ten, numbers)
