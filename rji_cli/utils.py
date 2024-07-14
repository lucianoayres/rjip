import sys

def print_message(message):
    """Prints a message to the console."""
    print(message)

def exit_with_message(message, code=0):
    """Prints a message and exits the program with the specified code."""
    print_message(message)
    sys.exit(code)
