import sys
import argparse
import json
from rji_cli.file_operations import file_exists, resolve_last_pick_file_path, create_empty_json_file, is_json_valid
from rji_cli.json_operations import validate_json_property, load_json, all_items_picked, exclude_json_items_in_common, get_random_item
from rji_cli.update_operations import update_last_pick_json
from rji_cli.utils import print_message, exit_with_message, print_json

def main(input_file, property_name, last_pick_file=None, update_last_pick=True):
    # Validate input file existence and format
    if not is_json_valid(input_file):
        exit_with_message(f"Invalid or non-existent JSON file: '{input_file}'", code=1)

    # Load input data from JSON file
    data = load_json(input_file)

    # Check if data is empty
    if not data:
        exit_with_message(f"Input JSON file '{input_file}' is empty.", code=1)

    # Validate property name if provided
    try:
        if property_name and not validate_json_property(input_file, property_name):
            exit_with_message(f"Property '{property_name}' is not valid in the input file '{input_file}'.", code=1)
    except ValueError as ve:
        exit_with_message(str(ve), code=1)

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

    # Print the new pick in JSON format
    print_json(new_pick)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process some JSON files.")
    parser.add_argument("input_file", help="The input JSON file.")
    parser.add_argument("property_name", help="The property name to validate.")
    parser.add_argument("last_pick_file", nargs="?", default=None, help="The last pick JSON file.")
    parser.add_argument("--no-update", dest="update_last_pick", action="store_false", help="Do not update the last pick file.")

    args = parser.parse_args()

    main(args.input_file, args.property_name, args.last_pick_file, args.update_last_pick)
