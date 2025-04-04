"""
Here are 4 practice problems to help you prepare for your PY119 written 
assessment, focusing on strings and string methods:
"""
"""
1.  Explain the difference between mutable and immutable data types in Python. 
How does this concept relate to strings? Provide an example that demonstrates 
string immutability.
"""
def change_the_snail(txt):
    return txt + ' are cool' 

snail = 'snails'
return_of_the_snail = change_the_snail(snail)

print(return_of_the_snail) # snails are cool
print(snail) # snails
"""
The difference between mutable and immutable data types is that immutable data
types in Python cannot be changed after creation while mutable ones can be.

In the `change_the_snail()` function, the string assigned to `snail` is passed
to the function on line 14. Then we attempt to change it inside the function
by concatenating it with another string inside the function. 

When we print the returning value of the function on line 16 and the value
assigned to `snail` on line 17, you can see that the function has created a 
new string object, and the original value of `'snails'` has not changed.
"""

"""
2. What will the following code output and why?
"""
text = "hello world"
result = text.replace("l", "*").split()
print(result[0][:3])

"""
The code prints:
he*

On line 35, the `replace()` string method is called on the string assigned to
the variable `text`. This would replace all the `'l'`s with `'*'`s, and thus
the returning string would be `'he**o wor*d'`. Then the `split()` method is
called on this string, splitting it into two strings as elements in a list, as
this method splits a string into a list of words using any whitespace as the 
default delimiter. The returning list is assigned to `result`.

Finally, slicing syntax is used to first access the first element (index 0 -
`[0]`) and extract the string from index 0 to 2 (indexes start from 0 in Python
and the stop values of slicing syntax - `3` - are exclusive), returning `'he*'`.
"""
