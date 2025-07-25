"""
Create a function that takes a list of numbers as an argument. For each number,
determine how many numbers in the list are smaller than it, and place the 
answer in a list. Return the resulting list.

When counting numbers, only count unique values. That is, if a number occurs 
multiple times in the list, it should only be counted once.
"""
"""
I: a list of numbers
O: a list of counts

Ex:
- [8, 1, 2, 2, 3] => [3, 0, 1, 1, 2]
    - [8, 1, 2, 3]
    - 8: 3 values are smaller
    - 1: 0 
    - 2: 1 is smaller
    - 3: 2 are smaller
- [7, 7, 7, 7] => [0, 0, 0, 0]
    - [7]
    - 7: none are smaller

Rules:
- for each number in the input list:
    - compare it to the rest of the numbers in the list
    - determine how many are smaller than the number
    - that count is what will go in the new list
- numbers that appear more than once should only be counted once
- output list has same length of input list

Breakdown:
- need a pared down, unique numbers list to compare each number to
    + turn into set for unique values
- new list to gather counts

Algo:
- counts = []
- for num in numbers:
    - append result of count_smaller(num, numbers) to counts
- return counts

-- helper (count_smaller) --
GOAL: count how many values are smaller in a unique set of values
I: integer - each value in input list (`num`)
O: integer - count of how many are smaller than input integer

- count = 0
- unique_values = turn numbers into a set
- for value in unique_values:
    - if value < num:
        - count += 1
- return count
"""
def count_smaller(num, numbers):
    unique_values = set(numbers)
    count = 0
    for value in unique_values:
        if value < num:
            count += 1
    return count

def smaller_numbers_than_current(numbers):
    return [count_smaller(num, numbers) for num in numbers]

print(smaller_numbers_than_current([8, 1, 2, 2, 3]) == [3, 0, 1, 1, 2])
print(smaller_numbers_than_current([7, 7, 7, 7]) == [0, 0, 0, 0])
print(smaller_numbers_than_current([6, 5, 4, 8]) == [2, 1, 0, 3])
print(smaller_numbers_than_current([1]) == [0])

my_list = [1, 4, 6, 8, 13, 2, 4, 5, 4]
result   = [0, 2, 4, 5, 6, 1, 2, 3, 2]
print(smaller_numbers_than_current(my_list) == result)
