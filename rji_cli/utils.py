import sys
import json

def print_message(message):
    """Prints a message to the console."""
    print(message)

def exit_with_message(message, code=0):
    """Prints a message and exits the program with the specified code."""
    print_message(message)
    sys.exit(code)

def print_json(data):
    """Print data in JSON format."""
    print(json.dumps(data))
