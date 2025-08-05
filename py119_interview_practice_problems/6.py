"""
Create a function that takes a string argument and returns a dict object in 
which the keys represent the lowercase letters in the string, and the values 
represent how often the corresponding letter occurs in the string.
"""
"""
I: a string
O: a dictionary of counts 

Rules:
- keys should be the lowercase letters in the input string
- values should be frequency of occurence of those letters
- uppercase and special characters should be ignored
- empty strings should return empty dictionaries

Breakdown:
- SET `counts` with an empty dictionary
- if the input is empty, return counts
- iterate through the string:
    - if it's a alphabetical letter and it's lowercase:
        - add to counts, along with its frequency count
- return counts
"""
def count_letters(txt):
    counts = {}
    for char in txt:
        if char.isalpha() and char.islower():
            counts[char] = counts.get(char, 0) + 1

    return counts

expected = {'w': 1, 'o': 2, 'e': 3, 'b': 1, 'g': 1, 'n': 1}
print(count_letters('woebegone') == expected) # True

expected = {'l': 1, 'o': 1, 'w': 1, 'e': 4, 'r': 2,
            'c': 2, 'a': 2, 's': 2, 'u': 1, 'p': 2}
print(count_letters('lowercase/uppercase') == expected) # True

expected = {'u': 1, 'o': 1, 'i': 1, 's': 1}
print(count_letters('W. E. B. Du Bois') == expected) # True

print(count_letters('x') == {'x': 1}) # True
print(count_letters('') == {}) # True
print(count_letters('!!!') == {}) # True
