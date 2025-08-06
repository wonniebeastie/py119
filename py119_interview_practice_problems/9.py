"""
Create a function that takes two string arguments and returns the number of 
times that the second string occurs in the first string. Note that overlapping
strings don't count: 'babab' contains 1 instance of 'bab', not 2.

You may assume that the second argument is never an empty string.
"""
# APPROACH 1
def count_substrings(full_str, substr):
    return full_str.count(substr)

print(count_substrings('babab', 'bab') == 1) # True
print(count_substrings('babab', 'ba') == 2) # True
print(count_substrings('babab', 'b') == 3) # True
print(count_substrings('babab', 'x') == 0) # True
print(count_substrings('babab', 'x') == 0) # True
print(count_substrings('', 'x') == 0) # True
print(count_substrings('bbbaabbbbaab', 'baab') == 2) # True
print(count_substrings('bbbaabbbbaab', 'bbaab') == 2) # True
print(count_substrings('bbbaabbbbaabb', 'bbbaabb') == 1) # True

"""
The string `.count()` method returns the occurrences of non-overlapping strings
already. But the interviewer may ask us to solve it without using the method
as the shortcut.

In that case, we can try to solve it manually:
"""
# APPROACH 2
def count_substrings2(full_str, substr):
    count = 0
    sub_len = len(substr)
    full_len = len(full_str)
    i = 0

    while i <= full_len - sub_len:
        if full_str[i:i+sub_len] == substr:
            count += 1
            i += sub_len
        else:
            i += 1

    return count

print(count_substrings2('babab', 'bab') == 1) # True
print(count_substrings2('babab', 'ba') == 2) # True
print(count_substrings2('babab', 'b') == 3) # True
print(count_substrings2('babab', 'x') == 0) # True
print(count_substrings2('babab', 'x') == 0) # True
print(count_substrings2('', 'x') == 0) # True
print(count_substrings2('bbbaabbbbaab', 'baab') == 2) # True
print(count_substrings2('bbbaabbbbaab', 'bbaab') == 2) # True
print(count_substrings2('bbbaabbbbaabb', 'bbbaabb') == 1) # True

"""
This second approach uses slicing to do a manual substring comparison at each
position. When a match is found, `count` is incremented and if the condition
is still truthy, skips ahead by the substring's length. Otherwise, the index is
incremented by 1.
"""

# APPROACH 3
def count_substrings3(full_str, substr):
    count = 0
    current_idx = 0

    while True:
        idx_at = full_str.find(substr, current_idx)
        
        if idx_at == -1:
            break

        count += 1
        current_idx = idx_at + len(substr)

    return count

print(count_substrings3('babab', 'bab') == 1) # True
print(count_substrings3('babab', 'ba') == 3) # True
print(count_substrings3('babab', 'b') == 3) # True
print(count_substrings3('babab', 'x') == 0) # True
print(count_substrings3('babab', 'x') == 0) # True
print(count_substrings3('', 'x') == 0) # True
print(count_substrings3('bbbaabbbbaab', 'baab') == 3) # True
print(count_substrings3('bbbaabbbbaab', 'bbaab') == 3) # True
print(count_substrings3('bbbaabbbbaabb', 'bbbaabb') == 1) # True

"""
This third approach uses manual indexing and an emulation of the do/while loop
(Python does not have a native one). We use the `.find()` string method to
look for the index position at which the substring starts in the full string,
but using the optional start parameter of where to begin the search.

If the substring is not found, then the find method returns -1. So if it's not 
found, the loop is broken and we return the current `count`.

But if it is found, then `count` is incremented by 1 and `current_index` is
assigned the resulting value from adding the index position to the length of
the substring, which `.find()` will use to "skip ahead" to the position to 
begin the search at the next iteration of the loop.
"""
