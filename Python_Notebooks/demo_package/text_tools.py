"""text_tools — submodule of demo_package (teaching example)."""


def shout(text):
    """Return the text in upper case with an exclamation mark."""
    return text.upper() + "!"


def word_count(text):
    """Return the number of words in the text."""
    return len(text.split())


def initials(full_name):
    """Return the initials of a full name, e.g. 'Alia Khan' -> 'A.K.'"""
    pieces = full_name.split()
    first_letters = []
    for piece in pieces:
        first_letters.append(piece[0].upper())
    return ".".join(first_letters) + "."
