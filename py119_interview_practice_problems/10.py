"""
Create a function that takes a string of digits as an argument and returns
the number of even-numbered substrings that can be formed. For example, in 
the case of '1432', the even-numbered substrings are '14', '1432', '4', 
'432', '32', and '2', for a total of 6 substrings.

If a substring occurs more than once, you should count each occurrence as 
a separate substring.
"""
"""
I: a string of digits
O: an integer, the count of all even-numbered substrings

Ex:
- '1432' => 6 
    - 14, 4 = 2
    - 1432, 432, 32, 2 = 4
    ----
    - 14 = index 1 + 1 = 2
    - 1432 = index 3 + 1 = 4

- '143232'=> 12
    - 14, 4 = 2
    - 14, 4, 1432, 2 = 4
    - 14, 4, 1432, 2, 143232, 2 = 6
    ----
    - 14 = index 1 + 1 = 2
    - 1432 = index 3 + 1 = 4
    - 143232 = index 5 + 1 = 6

Rules:
- order matters
- only focus on the even digits
- single-digit substrings are valid
- count substrings that occur more than once separately
- empty string should return 0

Breakdown:
- even numbers end in even numbers
----
- counter variable
- get index of every even digit
- add 1 to it to get the # of substrings that that number will create
- increment `count` by that result

Algo:
- SET `count` to 0
- iterate through digits digit by digit:
    - if the digit converted to a integer is an even number:
        - add 1 to index of digit,
        - increment count with it
"""
# Approach 1:
def even_substrings(digits):
    count = 0
    for idx, digit in enumerate(digits):
        if int(digit) % 2 == 0:
            count += (idx + 1)

    return count

print(even_substrings('1432') == 6) # True
print(even_substrings('3145926') == 16) # True
print(even_substrings('2718281') == 16) # True
print(even_substrings('13579') == 0) # True
print(even_substrings('143232') == 12) # True

"""
This first approach takes advantage of the mathematical fact that even numbers
always end in even digits. So this means we only need to process the substrings
that end in an even digit.

Using `'143232'` as the input:
- '143232'=> 12
    - 14, 4 = 2
    - 14, 4, 1432, 2 = 4
    - 14, 4, 1432, 2, 143232, 2 = 6
    ----
    - 14 = index 1 + 1 = 2
    - 1432 = index 3 + 1 = 4
    - 143232 = index 5 + 1 = 6

The pattern we see here is that the number of digits of an even number is the
same as the number of other even numbers it will generate (count by 1 
backwards for each even number).
(For each digit at `idx`, we can form `idx + 1` substrings that end with that
digit.)

length of substring == the # of even-numbered substrings it'll create
length of iterables == last index + 1

So we can solve this by incrementing `count` by that digit's index + 1.
"""

# Approach 2: 
def even_substrings2(digits):
    count = 0
    for i in range(len(digits)):
        if int(digits[i]) % 2 == 0:
            count += (i + 1)

    return count

print(even_substrings2('1432') == 6) # True
print(even_substrings2('3145926') == 16) # True
print(even_substrings2('2718281') == 16) # True
print(even_substrings2('13579') == 0) # True
print(even_substrings2('143232') == 12) # True

"""
This second approach is the same thing as the first one, but using a range
object instead, if `enumerate()` can't be used for whatever reason.
"""

# Approach 3:
def produce_nums(slce):
    result = []
    for idx in range(len(slce)):
        num = int(slce[:idx + 1])
        if num % 2 == 0:
            result.append(num)
    return result

def even_substrings3(digits):
    even_nums = []

    for idx in range(len(digits)):
        segment = produce_nums(digits[idx:])

        for num in segment:
            even_nums.append(num)

    return len(even_nums)

print(even_substrings3('1432') == 6) # True
print(even_substrings3('3145926') == 16) # True
print(even_substrings3('2718281') == 16) # True
print(even_substrings3('13579') == 0) # True
print(even_substrings3('143232') == 12) # True

"""
A brute force way of solving the problem - generating all possible even-
numbered substrings there can be and gathering them as integers in a list and
returning the length.
"""
