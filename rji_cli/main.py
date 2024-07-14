import sys
import json
from rji_cli.file_operations import file_exists, resolve_last_pick_file_path, create_empty_json_file
from rji_cli.json_operations import (
    load_json,
    validate_json_property,
    exclude_json_items_in_common,
    get_random_item,
    all_items_picked,
)
from rji_cli.update_operations import update_last_pick_json
from rji_cli.utils import print_message, exit_with_message

def main(input_file, property_name, last_pick_file=None, update_last_pick=True):
    # Validate input file existence
    if not file_exists(input_file):
        exit_with_message(f"Input file '{input_file}' not found.", code=1)

    # Validate property name
    if not validate_json_property(input_file, property_name):
        exit_with_message(f"Property '{property_name}' is not valid in the input file '{input_file}'.", code=1)

    # Load input data from JSON file
    try:
        data = load_json(input_file)
    except json.JSONDecodeError as e:
        exit_with_message(f"Error loading JSON from input file '{input_file}': {str(e)}", code=1)

    # Determine last pick file path
    last_pick_file_path = resolve_last_pick_file_path(input_file, last_pick_file)

    # Create last pick file if it doesn't exist
    if not file_exists(last_pick_file_path):
        print_message(f"Creating new last pick file: {last_pick_file_path}")
        create_empty_json_file(last_pick_file_path)

    # Load last picked items
    last_picks = load_json(last_pick_file_path)

    # Exclude items already picked
    remaining_items = exclude_json_items_in_common(data, last_picks, property_name)

    # Check if all items have been picked
    if all_items_picked(remaining_items):
        exit_with_message("All items have been picked.", code=0)

    # Get a new random item
    new_pick = get_random_item(remaining_items)

    # Update last pick file if specified
    if update_last_pick:
        update_last_pick_json(last_pick_file_path, new_pick)
        print_message(f"Updated last pick file with new pick: {new_pick}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        exit_with_message("Usage: python main.py <input_file> <property_name> [<last_pick_file>]", code=1)

    input_file = sys.argv[1]
    property_name = sys.argv[2]
    last_pick_file = sys.argv[3] if len(sys.argv) > 3 else None

    main(input_file, property_name, last_pick_file)
