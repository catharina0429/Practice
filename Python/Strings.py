"""Pangram"""
def is_pangram(sentence):
    a_to_z = "abcdefghijklmnopqrstuvwxyz"
    for char in a_to_z:
        if char not in sentence.lower():
            return False
    return True