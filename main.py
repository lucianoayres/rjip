import sys
import argparse
from rjip.file_operations import file_exists, resolve_last_pick_file_path, create_empty_json_file, is_json_valid
from rjip.json_operations import validate_json_property, load_json, all_items_picked, exclude_json_items_in_common, get_random_item
from rjip.update_operations import update_last_pick_json
from rjip.utils import print_json

# Error code mappings
ERROR_CODES = {
    "invalid_or_nonexistent_json_file": "invalid_or_nonexistent_json_file",
    "empty_input_json_file": "empty_input_json_file",
    "invalid_property_name": "invalid_property_name",
    "all_items_picked": "all_items_picked",
    "generic_error": "generic_error"
}

def main(input_file, property_name, last_pick_file=None, update_last_pick=True):
    try:
        # Validate input file existence and format
        if not is_json_valid(input_file):
            error_message = f"Invalid or non-existent JSON file: '{input_file}'"
            error_code = ERROR_CODES["invalid_or_nonexistent_json_file"]
            raise ValueError(error_message)

        # Load input data from JSON file
        data = load_json(input_file)

        # Check if data is empty
        if not data:
            error_message = f"Input JSON file '{input_file}' is empty."
            error_code = ERROR_CODES["empty_input_json_file"]
            raise ValueError(error_message)

        # Validate property name if provided
        if property_name and not validate_json_property(input_file, property_name):
            error_message = f"Property '{property_name}' is not valid in the input file '{input_file}'."
            error_code = ERROR_CODES["invalid_property_name"]
            raise ValueError(error_message)

        # Determine last pick file path
        last_pick_file_path = resolve_last_pick_file_path(input_file, last_pick_file)

        # Only create last pick file if it doesn't exist and --no-update was not passed
        if update_last_pick and not file_exists(last_pick_file_path):
            create_empty_json_file(last_pick_file_path)

        # Load last picked items if the file exists
        if file_exists(last_pick_file_path):
            last_picks = load_json(last_pick_file_path)
        else:
            last_picks = []

        # Exclude items already picked
        remaining_items = exclude_json_items_in_common(data, last_picks, property_name)

        # Check if all items have been picked
        if all_items_picked(remaining_items):
            error_message = "All items have been picked."
            error_code = ERROR_CODES["all_items_picked"]
            raise ValueError(error_message)

        # Get a new random item
        new_pick = get_random_item(remaining_items)

        # Update last pick file if specified
        if update_last_pick:
            update_last_pick_json(last_pick_file_path, new_pick)

        # Return the new pick in JSON format
        response = {"status": "success", "item": new_pick}
        print_json(response)
        sys.exit(0)
    
    except ValueError as ve:
        error_message = str(ve)
        response = {"status": "error", "message": error_message, "error_code": error_code}
        print_json(response)
        sys.exit(1)
    
    except Exception as e:
        error_message = "An unexpected error occurred."
        error_code = ERROR_CODES["generic_error"]
        response = {"status": "error", "message": error_message, "error_code": error_code}
        print_json(response)
        sys.exit(1)

def print_usage():
    print("rjip input_file property_name [last_pick_file] [--no-update]")
    print("\nArguments:\n")
    print("input_file         The path to the input JSON file containing the items to be picked.")
    print("property_name      A property name to validate within the JSON items.")
    print("last_pick_file     A file to store the last picked items (default: none). If no last_pick_file is specified, a new file will be created using the input file name as a prefix.")
    print("--no-update        A flag to disable updating the file that stores the last picked items.")
    print("\nrjip@1.0")
    sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Command-line tool designed to pick a random item from a JSON file while ensuring that each item is picked only once.")

    # Add arguments to the parser
    parser.add_argument("input_file", nargs="?", help="The input JSON file.")
    parser.add_argument("property_name", nargs="?", help="The property name to validate.")
    parser.add_argument("last_pick_file", nargs="?", default=None, help="The last pick JSON file.")
    parser.add_argument("--no-update", dest="update_last_pick", action="store_false", help="Do not update the last pick file.")

    # Parse arguments from command line
    args = parser.parse_args()

    # Check if required arguments are provided
    if not args.input_file or not args.property_name:
        print_usage()

    # Call main function with parsed arguments
    main(args.input_file, args.property_name, args.last_pick_file, args.update_last_pick)
