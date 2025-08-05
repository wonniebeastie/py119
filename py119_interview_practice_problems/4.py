"""
Create a function that takes a list of integers as an argument and returns a 
tuple of two numbers that are closest together in value. If there are multiple 
pairs that are equally close, return the pair that occurs first in the list.
--------
I: a list of numbers
O: a tuple pair of numbers (closest in distance our of all pairs)

Ex:
- [12, 22, 7, 17] => (12, 7)
    - 12, 22 = 10
    - 12, 7 = 5   <--- Smallest, but earliest
    - 12, 17 = 5  <--- Smallest  
    - 22, 7 = 15
    - 22, 17 = 5  <--- Smallest
    - 7, 17 = 15

Rules:
- each number in the input list must be paired with every other number
- then the differences between each pair should be compared
- the pair that has the smallest of the differences should be returned
- if multiple pairs are closest, then the one found earlier in the input
  list should be returned

Breakdown:
- SET `smallest_diff` to infinity
- SET `closest_pair` to an empty tuple
- iterate through each number in numbers, using i as the index 
  (from beginning of numbers to the length of numbers)
    - iterate through the rest of the list using j as the index
      (from i+1 to the length of numbers)
        - SET `difference` to the absolute value of numbers[i] & numbers[j]
        - if difference is less than smallest_diff:
            - UPDATE smallest_diff to have the value of difference
            - UPDATE closest_pair to current pair (numbers[i] & numbers[j])
- RETURN closest_pair
"""
# APPROACH 1
def closest_numbers(numbers):
    smallest_diff = float('inf')
    closest_pair = ()

    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            difference = abs(numbers[i] - numbers[j])
            if difference < smallest_diff:
                smallest_diff = difference
                closest_pair = (numbers[i], numbers[j])

    return closest_pair

print(closest_numbers([5, 25, 15, 11, 20]) == (15, 11)) # True
print(closest_numbers([19, 25, 32, 4, 27, 16]) == (25, 27)) # True
print(closest_numbers([12, 22, 7, 17]) == (12, 7)) # True

# APPROACH 2
# A less efficient alternative solution.
def get_difference(pair):
    return max(pair) - min(pair)

def closest_numbers2(numbers):
    pairs = []
    for idx1 in range(len(numbers) - 1):
        for idx2 in range(idx1 + 1, len(numbers)):
            pairs.append((numbers[idx1], numbers[idx2]))

    pairs.sort(key=get_difference)
    return pairs[0]

print(closest_numbers([5, 25, 15, 11, 20]) == (15, 11)) # True
print(closest_numbers([19, 25, 32, 4, 27, 16]) == (25, 27)) # True
print(closest_numbers([12, 22, 7, 17]) == (12, 7)) # True
