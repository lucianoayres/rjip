import json
import random

def load_json(file_path):
    """Load JSON data from file."""
    with open(file_path, 'r') as f:
        data = json.load(f)
        return data

def validate_json_property(file_path, property):
    """Validate JSON property existence."""
    data = load_json(file_path)
    if property not in data[0]:
        raise ValueError(f"Propert '{property}' JSON file '{file_path}'.")
    
def all_items_picked(remaining_items):
    """Check if all items have been picked."""
    return len(remaining_items) == 0

def exclude_json_items_in_common(json1_file_path, json2_file_path, property_name):
    """Exclude items common with another JSON based on property."""
    filtered_json = [item for item in json1_file_path if item[property_name] not in {item2[property_name] for item2 in json2_file_path}]
    return filtered_json

def get_random_item(json_data):
    """Get a random item from JSON data."""
    if not json_data:
        raise ValueError("JSON data is empty")
    return random.choice(json_data)