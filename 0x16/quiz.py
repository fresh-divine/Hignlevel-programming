#!/usr/bin/python3
"""A module that accepts a sentence and performs string operations."""


def get_first_character(text):
    """Return the first character of the text."""
    return text[0]


def get_last_character(text):
    """Return the last character using negative indexing."""
    return text[-1]


def get_first_word(text):
    """Return the first word of the text."""
    for i in range(len(text)):
        if text[i] == " ":
            return text[:i]
    return text


def get_last_word(text):
    """Return the last word of the text."""
    start = len(text) - 1

    while start >= 0 and text[start] == " ":
        start -= 1

    end = start

    while start >= 0 and text[start] != " ":
        start -= 1

    return text[start + 1:end + 1]


def reverse_string(text):
    """Return the text reversed using slicing."""
    return text[::-1]


def every_other_character(text):
    """Return every second character using step slicing."""
    return text[::2]


def get_middle(text):
    """Return the middle character or middle two characters."""
    length = len(text)
    middle = length // 2

    if length % 2 == 1:
        return text[middle]
    return text[middle - 1:middle + 1]


def character_count(text):
    """Return the total number of characters in the text."""
    return len(text)


def display_results(text, results):
    """Display all text-processing results in a clean format."""
    print("\nText Processing Results")
    print("-----------------------")
    print("Original text:", text)
    print("First character:", results["first_character"])
    print("Last character:", results["last_character"])
    print("First word:", results["first_word"])
    print("Last word:", results["last_word"])
    print("Reversed:", results["reversed"])
    print("Every other character:", results["every_other"])
    print("Middle:", results["middle"])
    print("Character count:", results["character_count"])


def main():
    """Coordinate the text-processing program."""
    text = input("Please type your sentence: ")

    if not text:
        print("Error: The sentence cannot be empty.")
        return

    results = {
        "first_character": get_first_character(text),
        "last_character": get_last_character(text),
        "first_word": get_first_word(text),
        "last_word": get_last_word(text),
        "reversed": reverse_string(text),
        "every_other": every_other_character(text),
        "middle": get_middle(text),
        "character_count": character_count(text),
    }

    display_results(text, results)


if __name__ == "__main__":
    main()