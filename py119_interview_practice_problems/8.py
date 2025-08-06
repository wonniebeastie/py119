"""
Create a function that takes a non-empty string as an argument. The string 
consists entirely of lowercase alphabetic characters. The function should 
return the length of the longest vowel substring. The vowels of interest are 
"a", "e", "i", "o", and "u".
"""
"""
I: a string, non-empty, all lowercase alphabetic
O: an integer, the length of the longest vowel substring

Ex:
- 'beauteous' => 3
    - eau = 3
    - eou = 3
- 'miaoued' => 5
    - iaoue = 5

Rules:
- vowels are 'aeiou'
- no need to worry about cases since all are lowercase

Breakdown:
- SET `VOWELS` to 'aeiou'
- SET `longest_len` to 0
- SET `current_len` to 0
- iterate through each character in txt:
    - if the character is a vowel:
        - increment current_len by 1
    - else:
        - reset current_len to 0
    - SET `longest_len` to whichever is bigger: the longest_len or current_len
- return longest_len

Step-Through:
'beauteous'
longest = 3
current = 0
"""
def longest_vowel_substring(txt):
    VOWELS = 'aeiou'
    longest_len = 0
    current_len = 0

    for char in txt:
        if char in VOWELS:
            current_len += 1
        else:
            current_len = 0
        longest_len = max(longest_len, current_len)
    
    return longest_len

print(longest_vowel_substring('cwm') == 0) # True
print(longest_vowel_substring('many') == 1) # True
print(longest_vowel_substring('launchschoolstudents') == 2) # True
print(longest_vowel_substring('eau') == 3) # True
print(longest_vowel_substring('beauteous') == 3) # True
print(longest_vowel_substring('sequoia') == 4) # True
print(longest_vowel_substring('miaoued') == 5) # True

"""
NOTE:
We don't need the actual string because we're returning the length of the
string only. So we just need to keep two counter variables - one for the total
running longest length, and one for the current length.

The current length gets reset whenever the loop encounters a consonant. The
longest length stays even if the current length gets reset to 0.
"""
