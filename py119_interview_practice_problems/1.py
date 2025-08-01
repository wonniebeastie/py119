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
"""

# APPROACH 1: PRE-CALCULATION & MAP
"""
Breakdown:
- this approach is based on the fundamental properties of a sorted list of
  unique numbers.
- if we sort a list of unique numbers in ascending order:
    - every element at a given index is guaranteed to be larger than all 
      elements that come before it
    - list indices are zero-based, so the number of elements that come before
      any index i is exactly i
    - ex: [6, 5, 4, 8]
        - sort [4, 5, 6, 8]
        - index: 0, num: 4 (there are 0 numbers smaller than 4)
        - index: 2, num: 6 (there are 2 numbers smaller than 6)
        - and so on...

Algo:
- turn into set to get unique numbers 
    - `set()`
- sort in ascending order 
    - `sorted()` function returns a list (name it `sorted_unique_nums`)
- map the numbers from sorted_unique_nums to their index using a dictionary
    - keys = numbers
    - values = index
    - `enumerate()` since we're working with a list, for both index & value
    - name it `count_map`
- result = []
- for num in numbers (original input list):
    - get count_map[num] (this gets the associated value for that number)
    - append it to result
- return result

Step-Through:
- [8, 1, 2, 2, 3] 
- {8, 1, 2, 3} 
- [1, 2, 3, 8] 
- {1: 0, 2: 1, 3: 2, 8: 3}
- iterate through input list, get values (index)
  [3, 0, 1, 1, 2]

NOTE:
This dictionary-approach is the most efficient as the input size grows.
"""
def smaller_numbers_than_current(numbers):
    sorted_unique_nums = sorted(set(numbers))
    count_map = {num: idx for idx, num in enumerate(sorted_unique_nums)}
    return [count_map[num] for num in numbers]

print(smaller_numbers_than_current([8, 1, 2, 2, 3]) == [3, 0, 1, 1, 2])
print(smaller_numbers_than_current([7, 7, 7, 7]) == [0, 0, 0, 0])
print(smaller_numbers_than_current([6, 5, 4, 8]) == [2, 1, 0, 3])
print(smaller_numbers_than_current([1]) == [0])

my_list = [1, 4, 6, 8, 13, 2, 4, 5, 4]
result   = [0, 2, 4, 5, 6, 1, 2, 3, 2]
print(smaller_numbers_than_current(my_list) == result)


# APPROACH 2: SORT & MAP
"""
Breakdown:
- create unique list of integers from numbers
- sort it in ascending order
- iterate through sorted list
- get index position for each number
- populate new list with the indices

Algo:
unique_nums = numbers turned into a set
turn unique_nums into a list so we can sort it
sort unique_nums in ascending order

for num in numbers:
    append index of num to `counts` list
return counts
"""

def smaller_numbers_than_current2(numbers):
    sorted_unique_nums = sorted(list(set(numbers)))
    # For each number in input list, find its index in the sorted, unique version
    return [sorted_unique_nums.index(num) for num in numbers]

print(smaller_numbers_than_current2([8, 1, 2, 2, 3]) == [3, 0, 1, 1, 2]) # True
print(smaller_numbers_than_current2([7, 7, 7, 7]) == [0, 0, 0, 0]) # True
print(smaller_numbers_than_current2([6, 5, 4, 8]) == [2, 1, 0, 3]) # True
print(smaller_numbers_than_current2([1]) == [0]) # True

my_list = [1, 4, 6, 8, 13, 2, 4, 5, 4]
result   = [0, 2, 4, 5, 6, 1, 2, 3, 2]
print(smaller_numbers_than_current2(my_list) == result) # True


# APPROACH 3: DIRECT COUNTING
"""
Breakdown:
- need a pared down, unique numbers list to compare each number to
    + turn into set for unique values
- new list to gather counts

Main Algo:
counts = []
unique_nums = turn numbers into a set
for num in numbers:
    append count_smaller(num, unique_nums) to counts
return counts

Helper Algo:
I: integer - each value in input list (`num`)
O: integer - count of how many are smaller than input integer
GOAL: Count how many values are smaller in a unique set of values

count = 0
for unique_num in unique_nums:
    if num is greater than unique_num:
        increment count by 1
return count
"""
def count_smaller(num, unique_nums):
    count = 0
    for unique_num in unique_nums:
        if num > unique_num:
            count += 1
    return count

def smaller_numbers_than_current3(numbers):
    unique_nums = set(numbers)
    return [count_smaller(num, unique_nums) for num in numbers]

print(smaller_numbers_than_current3([8, 1, 2, 2, 3]) == [3, 0, 1, 1, 2]) # True
print(smaller_numbers_than_current3([7, 7, 7, 7]) == [0, 0, 0, 0]) # True
print(smaller_numbers_than_current3([6, 5, 4, 8]) == [2, 1, 0, 3]) # True
print(smaller_numbers_than_current3([1]) == [0]) # True

my_list = [1, 4, 6, 8, 13, 2, 4, 5, 4]
result   = [0, 2, 4, 5, 6, 1, 2, 3, 2]
print(smaller_numbers_than_current3(my_list) == result) # True
