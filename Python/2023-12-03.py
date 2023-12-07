def convert(number):
    res = ''
    if number % 3 == 0:
        res += "Pling"
    if number % 5 == 0:
        res = res + "Plang"
    if number % 7 == 0:
        res = res + "Plong"
    if res == "":
        res = str(number)
    return res

print(convert(1))
print(convert(49))
print(convert(52))
print(convert(105))

"""strings practice"""
def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.

    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """
    return "un" + word


def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended.

    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with
            prefix applied.

    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separated
     by ' :: '.

    For example: list('en', 'close', 'joy', 'lighten'),
    produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    """
    prefix = vocab_words[0]
    tmp = [prefix + i for i in vocab_words[1:]]
    tmp.insert(0, prefix)
    return " :: ".join(tmp)

def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """
    if word[-5:] == "iness":
        return word[:len(word)-5] + "y"
    return word[:-4]  

def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set.", 2) becomes "darken".
    """
    tmp = sentence.split()[index]
    if tmp[-1] == ".":
        return tmp[:len(tmp)-1] + "en"
    return tmp + "en"

def reverse(text):
    return text[::-1]

tmp = "Hello world!"
reverse(tmp)

"""Grains"""
def square(number):
    if number in range(1, 65):
        return 2 ** (number -1)
    raise ValueError("Invalid Input! it must be between 1 and 64")

def total():
    total = 0
    for i in range(1, 65):
        total = total + square(i)
    return total