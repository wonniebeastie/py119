"""
Write a function that takes a list of numbers and a threshold value as 
arguments. The function should return a new list containing only the numbers 
from the original list that are greater than the threshold.
"""
"""
I: a list (of numbers)
I: an integer (threshold value)
O: a new list 

✱ RULES ✱
- returned list should only contain numbers greater than the 2nd input.
- returned list should be a new list.

✱ POSSIBLE DS / BRAINSTORM ✱
- an empty list to contain the results

✱ ALGORITHM ✱
[] initialize empty list `result`
[] for num in `numbers`:
    [] if num is greater than `threshold`:
        [] append num to result
[] return result
"""

def filter_above_threshold(numbers, threshold):
    result = []
    for num in numbers:
        if num > threshold:
            result.append(num)
    return result

# Test cases
print(filter_above_threshold([1, 5, 2, 8, 3], 3))  # Expected: [5, 8]
print(filter_above_threshold([10, 20, 30], 25))    # Expected: [30]
print(filter_above_threshold([5, 10, 15], 20))     # Expected: []

