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

"""strings"""
def add_prefix_un(word):
    return 'un' + word
print(add_prefix_un("happy"))
print(add_prefix_un("manageable"))

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
    res = []
    res = add_prefix_un(vocab_words[1:-1])
    res.append(prefix)
    return res
print(make_word_groups['en', 'close', 'joy', 'lighten'])