"""
Create a function that takes a list of integers as an argument. The function 
should return the minimum sum of 5 consecutive numbers in the list. If the list
contains fewer than 5 elements, the function should return `None`.
"""
"""
I: a list of numbers
O: an integer, the minimum sum OR None (fewer than 5 elements)

Ex:
- [1, 2, 3, 4, 5, -5] => 9
    - 1 + 2 + 3 + 4 + 5 = 15
    - 2 + 3 + 4 + 5 + -5 = 9
    - 9 is smaller
- [1, 2, 3, 4, 5, 6] => 15
    - 1 + 2 + 3 + 4 + 5 = 15
    - 2 + 3 + 4 + 5 + 6 = 20
    - 15 is smaller

Rules:
- if there are fewer than 5 elements, function should return None
- get sums of all possible groups of 5 consecutive elements
- return the smallest one 

Breakdown:
- if the length of `numbers` is less than 5, return None
- mini_sum = sum of the first slice of 5 consecutive numbers of numbers
- for each num in a range of 1 to (length of numbers - 4):
    - sum_of_slice = sum all numbers in numbers[num:num+5]
    - if sum_of_slice is less than mini_sum:
        - then assign the value of sum_of_slice to mini_sum
- return mini_sum
"""
# APPROACH 1
def minimum_sum(numbers):
    if len(numbers) < 5:
        return None
    
    mini_sum = sum(numbers[:5])
    for num in range(1, len(numbers) - 4):
        sum_of_slice = sum(numbers[num:num+5])
        if sum_of_slice < mini_sum:
            mini_sum = sum_of_slice
    return mini_sum

# These tests should each print True.
print(minimum_sum([1, 2, 3, 4]) is None) # True
print(minimum_sum([1, 2, 3, 4, 5, -5]) == 9) # True
print(minimum_sum([1, 2, 3, 4, 5, 6]) == 15) # True
print(minimum_sum([55, 2, 6, 5, 1, 2, 9, 3, 5, 100]) == 16) # True
print(minimum_sum([-1, -5, -3, 0, -1, 2, -4]) == -10) # True

# APPROACH 2
def minimum_sum2(numbers):
    if len(numbers) < 5:
        return None
    
    sums = [sum(numbers[idx:idx + 5]) for idx in range(len(numbers) - 4)]
    
    return min(sums)

print(minimum_sum2([1, 2, 3, 4]) is None) # True
print(minimum_sum2([1, 2, 3, 4, 5, -5]) == 9) # True
print(minimum_sum2([1, 2, 3, 4, 5, 6]) == 15) # True
print(minimum_sum2([55, 2, 6, 5, 1, 2, 9, 3, 5, 100]) == 16) # True
print(minimum_sum2([-1, -5, -3, 0, -1, 2, -4]) == -10) # True

"""
Approach 2 has a higher memory usage than Approach 1, as Approach 1 creates
an intermediate list to hold all the sums before `min()` is called. If the
input lists are very large, this can use much more memory.
"""

# APPROACH 3
"""
Algo:
1. EDGE CASE: If the length of `numbers` is less than 5, return `None`.
2. SET `current_sum`:
    Compute the sum of the first slice of 5 consecutive numbers
3. SET `min_sum` to `current_sum`
4. LOOP: Slide a 5-element window one position at a time through the input list
    - For each new position:
        - UPDATE `current_sum` by subtracting the element that's leaving the 
          window & adding the new element entering the window.
        - If the new `current_sum` is less than `min_sum`:
            - UPDATE `min_sum` to `current_sum`
4. RETURN `min_sum`
"""
def minimum_sum3(numbers):
    if len(numbers) < 5:
        return None

    current_sum = sum(numbers[:5])
    min_sum = current_sum

    for i in range(1, len(numbers) - 4):
        current_sum = current_sum - numbers[i-1] + numbers[i+4]
        if current_sum < min_sum:
            min_sum = current_sum

    return min_sum

print(minimum_sum3([1, 2, 3, 4]) is None) # True
print(minimum_sum3([1, 2, 3, 4, 5, -5]) == 9) # True
print(minimum_sum3([1, 2, 3, 4, 5, 6]) == 15) # True
print(minimum_sum3([55, 2, 6, 5, 1, 2, 9, 3, 5, 100]) == 16) # True
print(minimum_sum3([-1, -5, -3, 0, -1, 2, -4]) == -10) # True

"""
The third "Sliding Window" approach is less readable than the other two, but
it performs much better for large lists because it avoids recalculating sums
and only does one subtraction and one addition per step.

It also uses less memory. 
"""
