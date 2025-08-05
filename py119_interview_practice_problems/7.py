"""
Create a function that takes a list of integers as an argument and returns the 
number of identical pairs of integers in that list. For instance, the number of
identical pairs in `[1, 2, 3, 2, 1]` is 2: occurrences each of both `2` and 
`1`.

If the list is empty or contains exactly one value, return 0.

If a certain number occurs more than twice, count each complete pair once. For 
instance, for `[1, 1, 1, 1]` and `[2, 2, 2, 2, 2]`, the function should return 
2. The first list contains two complete pairs while the second has an extra `2`
that isn't part of the other two pairs.
"""
"""
I: a list of numbers or empty list
O: an integer, the number of identical pairs of integers

Ex:
- [2, 7, 1, 8, 2, 8, 1, 8, 2, 8, 4] => 4
    - 2: 3 = 3//2 = 1
    - 7: 1 = 1//2 = 0
    - 1: 2 = 2//2 = 1
    - 8: 4 = 2
    - 4: 1 = 0
    - add up all pairs 2 + 1 + 1 = 4

Rules:
- if list is empty or contains only one element, return 0
- a pair is two identical numbers
- if a pair occurs more than once, each should be counted as 1

Breakdown:
- if the length of `numbers` is less than 2:
    - return 0
- create a frequency map using a dictionary `counts`
- get the values view object
    - iterate through the values
        - floor divide each value by 2
        - add up the results
- return the sum
"""
def pairs(numbers):
    if len(numbers) < 2:
        return 0

    counts = {}
    for number in numbers:
        counts[number] = counts.get(number, 0) + 1

    return sum(count//2 for count in counts.values())

print(pairs([3, 1, 4, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7]) == 3) # True
print(pairs([2, 7, 1, 8, 2, 8, 1, 8, 2, 8, 4]) == 4) # True
print(pairs([]) == 0) # True
print(pairs([23]) == 0) # True
print(pairs([997, 997]) == 1) # True
print(pairs([32, 32, 32]) == 1) # True
print(pairs([7, 7, 7, 7, 7, 7, 7]) == 3) # True
