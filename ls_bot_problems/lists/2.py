# Create a function that concatenates two lists by appending each element of the 
# second list to the first list one by one.
"""
I: a list
I: another list
O: a list that is the sum of the input lists

✱ RULES ✱
- the second list must be added element by element to the first list

✱ QUESTIONS ✱
- what if the 2nd list is empty?
    + return the first list as is.
- does the returned list have to be a new list? 

✱ ALGORITHM ✱
[] if list2 is not empty:
    for element in list2:
        append element to list1

[] return list1
"""
def custom_concat(list1, list2):
    for element in list2:
        list1.append(element)

    return list1

print(custom_concat([1, 2], [3, 4]))        # Expected: [1, 2, 3, 4]
print(custom_concat([], ['a', 'b', 'c']))   # Expected: ['a', 'b', 'c']
print(custom_concat([True, False], []))     # Expected: [True, False]
