import string


def is_pangram(sentence):
    """Check if all the characters in the alphabet (a - z) is used in a given sentence."""
    # Convert the input to all lower case letters.
    lower_case_sentence = sentence.lower()

    # Get a list of all the ASCII lower case letters i.e. a-z.
    all_lower_case_ascii_letters = string.ascii_lowercase

    set_of_letters_in_sentence = set()                     # Start with an empty set.
    for c in lower_case_sentence:
        if c in all_lower_case_ascii_letters:
            set_of_letters_in_sentence.add(c)              # Attempt to add each symbol that is a letter into the set.

    # In a pangram so will the number of letters equal the number of letters in the alphabet.
    if len(set_of_letters_in_sentence) == len(all_lower_case_ascii_letters):
        return True
    else:
        return False

