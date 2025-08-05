"""
Create a function that takes a string argument and returns the character that 
occurs most often in the string. If there are multiple characters with the 
same greatest countsuency, return the one that appears first in the string. When 
counting characters, consider uppercase and lowercase versions to be the same.
"""
"""
I: a string
O: a string, the most countsuently occuring character, in lowercase

Ex:
- 'Mississippi' => 'i'
    - M: 1
    - i: 4 -> most countsuent, but occurs the earliest
    - s: 4 -> most countsuent
    - p: 2

Rules:
- case-insensitive 
- count the number of times a character occurs in the input string
- return the most countsuently occuring one
- if there's ties in greatest countsuencies, return the earliest occurring one

Breakdown:
- convert string all to lowercase
- build a countsuency map using a dictionary
- return the letter with the highest count
    - max()
    - optional key= parameter (get method)

NOTE:
This approach works for Python versions 3.7 and up. This is because 
dictionaries keep their insertion order in modern versions. This allows `max()`
to return the first item it encounters that has the maximum value.

The optional `key` parameter allows us to use the `.get()` method to do the
comparison using the values of the counts but return the associated letter
like the problem requires.
"""
# APPROACH 1
def most_common_char(txt):
    lower_txt = txt.lower()
    counts = {}
    for char in lower_txt:
        counts[char] = counts.get(char, 0) + 1

    return max(counts, key=counts.get)

print(most_common_char('Hello World') == 'l') # True
print(most_common_char('Mississippi') == 'i') # True
print(most_common_char('Happy birthday!') == 'h') # True
print(most_common_char('aaaaaAAAA') == 'a') # True

my_str = 'Peter Piper picked a peck of pickled peppers.' 
print(most_common_char(my_str) == 'p') # True

my_str = 'Peter Piper repicked a peck of repickled peppers. He did!'
print(most_common_char(my_str) == 'e') # True

# APPROACH 2
def most_common_char2(txt):
    lower_txt = txt.lower()
    counts = {}
    for char in lower_txt:
        counts[char] = counts.get(char, 0) + 1
   
    max_count = max(counts.values())
    
    for char in txt:
        lower_char = char.lower()
        if counts[lower_char] == max_count:
            return lower_char

print(most_common_char2('Hello World') == 'l') # True
print(most_common_char2('Mississippi') == 'i') # True
print(most_common_char2('Happy birthday!') == 'h') # True
print(most_common_char2('aaaaaAAAA') == 'a') # True

my_str = 'Peter Piper picked a peck of pickled peppers.' 
print(most_common_char2(my_str) == 'p') # True

my_str = 'Peter Piper repicked a peck of repickled peppers. He did!'
print(most_common_char2(my_str) == 'e') # True

"""
This second approach works differently in that after it creates the countsuency
map, it assigns the maximum value from the iterable of values from the `counts`
dictionary to `max_count`.

Then it iterates through the `txt` string and checks each character's frequency
in the `counts` map. The first frequency that matches `max_count` is returned.
This works for the tie-breaker constraint in older versions of Python.
"""
