# Create a function that takes a nested list (a list of lists) and returns a 
# flattened version of the list using the `append` method.
"""
I: a list (with nested lists)
O: a list (a flattened version of input list)

✱ QUESTIONS ✱
- 

✱ POSSIBLE DS / BRAINSTORM ✱
- an empty list to collect the items into

✱ ALGORITHM ✱
[] initialize `flattened_list` with an empty list
[] for sublist in `nested_list`:
    for element in sublist:
        append element to flattened_list
[] return flattened_list
"""
# Using a traditional `for` loop
def flatten_list(nested_list):
    flattened_list = []
    for sublist in nested_list:
        for element in sublist:
            flattened_list.append(element)
    return flattened_list

# Using a nested comprehension
def flatten_list2(nested_list):
    return [element for sublist in nested_list
             for element in sublist]

# Test cases
print(flatten_list([[1, 2], [3, 4]]))           # Expected: [1, 2, 3, 4]
print(flatten_list([[5], [], [6, 7, 8]]))       # Expected: [5, 6, 7, 8]
print(flatten_list([['a', 'b'], ['c'], ['d']])) # Expected: ['a', 'b', 'c', 'd']

print(flatten_list2([[1, 2], [3, 4]]))           # Expected: [1, 2, 3, 4]
print(flatten_list2([[5], [], [6, 7, 8]]))       # Expected: [5, 6, 7, 8]
print(flatten_list2([['a', 'b'], ['c'], ['d']])) # Expected: ['a', 'b', 'c', 'd']
