# Write a function that takes a list of strings and returns a new list 
# containing the lengths of each string. Use the `append` method in your 
# solution.
"""
I: a list (of strings)
O: a new list (of integers)

✱ RULES ✱
- output list should contain the lengths of each string in the input list
- output list must be a new list object

✱ POSSIBLE DS / BRAINSTORM ✱
- an empty list to contain the lengths `string_lengths`

✱ ALGORITHM ✱
[] initialize empty list - `string_lengths`
[] for string in strings:
    [] append the length of string to string_lengths
[] return string_lengths
"""

def string_lengths(strings):
    string_lengths = []

    for string in strings:
        string_lengths.append(len(string))

    return string_lengths

# Test cases
print(string_lengths(['hello', 'world']))          # Expected: [5, 5]
print(string_lengths(['python', '', 'is', 'fun'])) # Expected: [6, 0, 2, 3]
print(string_lengths([]))                          # Expected: []
