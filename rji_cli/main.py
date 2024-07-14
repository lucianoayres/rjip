import sys
import json
import os
from rji_cli.file_operations import file_exists
from rji_cli.json_operations import (
    load_json,
    validate_json_property,
    exclude_json_items_in_common,
    get_random_item,
)
from rji_cli.update_operations import update_last_pick_json

# TODO: Refactor to file_operations.py
def resolve_last_pick_file_path(input_file, last_pick_file=None):
    """Resolve the path for the last pick file, creating it if not provided."""
    if last_pick_file:
        return last_pick_file
    else:
        input_filename = os.path.basename(input_file)
        return f"last_pick_{input_filename}"

def main(input_file, property_name, last_pick_file=None, update_last_pick=True):
    # Validate input file existence
    if not file_exists(input_file):
        print(f"Input file '{input_file}' not found.")
        sys.exit(1)

    # Validate property name
    if not validate_json_property(input_file, property_name):
        print(f"Property '{property_name}' is not valid in the input file '{input_file}'.")
        sys.exit(1)

    # Load input data from JSON file
    try:
        data = load_json(input_file)
    except json.JSONDecodeError as e:
        print(f"Error loading JSON from input file '{input_file}': {str(e)}")
        sys.exit(1)

    # Determine last pick file path
    last_pick_file_path = resolve_last_pick_file_path(input_file, last_pick_file)

    # Create last pick file if it doesn't exist
    if not file_exists(last_pick_file_path):
        print(f"Creating new last pick file: {last_pick_file_path}")
        
        # TODO: Refactor to file_operations.py
        with open(last_pick_file_path, 'w') as file:
            json.dump([], file)

    # Load last picked items
    last_picks = load_json(last_pick_file_path)

    # Exclude items already picked
    remaining_items = exclude_json_items_in_common(data, last_picks, property_name)

    # Check if all items have been picked
    # TODO: Refactor to json_operations.py
    if len(remaining_items) == 0:
        print("All items have been picked.")
        sys.exit(0)

    # Get a new random item
    new_pick = get_random_item(remaining_items)

    # Update last pick file if specified
    if update_last_pick:
        update_last_pick_json(last_pick_file_path, new_pick)
        print(f"Updated last pick file with new pick: {new_pick}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python main.py <input_file> <property_name> [<last_pick_file>]")
        sys.exit(1)

    input_file = sys.argv[1]
    property_name = sys.argv[2]
    last_pick_file = sys.argv[3] if len(sys.argv) > 3 else None

    main(input_file, property_name, last_pick_file)
