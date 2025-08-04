"""
Create a function that takes a string argument and returns a copy of the string
with every second character in every third word converted to uppercase. Other 
characters should remain the same.
"""
"""
I: a string
O: the same string, with every second char of every third word uppercased

Ex:
- 'Lorem Ipsum is simply dummy text of the printing world'
=> 'Lorem Ipsum iS simply dummy tExT of the pRiNtInG world'
    - is -> iS
    - text -> tExT
    - printing -> pRiNtInG

Rules:
- other characters to remain the same
- the first char of each third word is lowercased

Breakdown:
- Split `txt` into a list of words 
    - SET to `words`
- Empty list to hold transformed words 
    - SET to `transformed_words`
- Iterate through `words` keeping track of both the index and word -
    - for every third word:
        - call transform_word(word)
        - append returned result to `transformed_words`
    - for all other words:
        - append to `transformed_words` as is
- Join all words in `transformed_words` together into a single string, using
  a space as the delimiter, and return it.

-- Helper (transform_word) --
I: a word, as a string
O: the same word with every other char uppercased

- SET `result` to empty string
- iterate through `word` keeping track of both the index & character:
    - if the index is odd:
        - change the char to upper case
        - concatenate to `result`
    - else:
        - concatenate to `result` as is
- RETURN `result`
"""
def transform_word(word):
    result = ''

    for idx, char in enumerate(word):
        if idx % 2 != 0:
            result += char.upper()
        else:
            result += char

    return result

def to_weird_case(txt):
    words = txt.split()
    transformed_words = []

    for idx, word in enumerate(words):
        if (idx + 1) % 3 == 0:
            transformed_words.append(transform_word(word))
        else:
            transformed_words.append(word)

    return ' '.join(transformed_words)

original = 'Lorem Ipsum is simply dummy text of the printing world'
expected = 'Lorem Ipsum iS simply dummy tExT of the pRiNtInG world'
print(to_weird_case(original) == expected) # True

original = 'It is a long established fact that a reader will be distracted'
expected = 'It is a long established fAcT that a rEaDeR will be dIsTrAcTeD'
print(to_weird_case(original) == expected) # True

print(to_weird_case('aaA bB c') == 'aaA bB c') # True

original = "Mary Poppins' favorite word is supercalifragilisticexpialidocious"
expected = "Mary Poppins' fAvOrItE word is sUpErCaLiFrAgIlIsTiCeXpIaLiDoCiOuS"
print(to_weird_case(original) == expected) # True

# REFACTORED
def to_weird_case2(txt):
    def transform_word(word):
        """
        GOAL: uppercase every other character in a word
        I: a word, as a string
        O: transformed word as a string
        """
        return "".join(
            char.upper() if idx % 2 != 0 else char
            for idx, char in enumerate(word)
        )

    words = txt.split()

    transformed_words = [transform_word(word) if (idx+1) % 3 == 0 else word
                         for idx, word in enumerate(words)]

    return " ".join(transformed_words)

original = 'Lorem Ipsum is simply dummy text of the printing world'
expected = 'Lorem Ipsum iS simply dummy tExT of the pRiNtInG world'
print(to_weird_case2(original) == expected) # True

original = 'It is a long established fact that a reader will be distracted'
expected = 'It is a long established fAcT that a rEaDeR will be dIsTrAcTeD'
print(to_weird_case2(original) == expected) # True

print(to_weird_case2('aaA bB c') == 'aaA bB c') # True

original = "Mary Poppins' favorite word is supercalifragilisticexpialidocious"
expected = "Mary Poppins' fAvOrItE word is sUpErCaLiFrAgIlIsTiCeXpIaLiDoCiOuS"
print(to_weird_case2(original) == expected) # True
