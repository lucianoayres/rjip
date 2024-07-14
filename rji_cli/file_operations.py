import os 
import json

def file_exists(file_path):
    """Check if a file exists"""
    try:
        with open(file_path, 'r') as f:
            return True
    except FileNotFoundError:
        return False
    
def resolve_last_pick_file_path(input_file, last_pick_file=None):
    """Resolve the path for the last pick file, creating it if not provided."""
    if last_pick_file:
        return last_pick_file
    else:
        input_filename = os.path.basename(input_file)
        return f"last_pick_{input_filename}"
    
def create_empty_json_file(file_path):
    """Creates an empty JSON file at the specified path."""
    with open(file_path, 'w') as file:
        json.dump([], file)

def is_json_valid(file_path):
    """Check if the file exists and is valid JSON."""
    if not file_exists(file_path):
        return False

    try:
        with open(file_path, 'r') as f:
            json.load(f)
    except json.JSONDecodeError:
        return False

    return True

