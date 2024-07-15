# rJip: Random JSON Item Picker

Command-line tool designed to pick a random item from a JSON file while ensuring that each item is picked only once. It keeps track of previously picked items to maintain uniqueness until all items have been picked at least once.

## Features

-   Random Item Selection: Retrieves a random item from a specified JSON file.
-   Tracking Last Picks: Maintains a record of previously picked items to avoid duplicates.
-   Property Validation: Validates a specified property name within the JSON data.
-   Error Handling: Includes specific error codes for different validation and operational errors.

## Usage

To use the tool, execute `rjip` with the following parameters:

```bash
$ python main.py input_file property_name [last_pick_file] [--no-update]
```

-   `input_file`: The path to the input JSON file containing the items to be picked.
-   `property_name`: A property name to validate within the JSON items.
-   `last_pick_file`: An optional file to store the last picked items (default: none). If no last_pick_file is specified, a new file will be created using the input file name as a prefix.
-   `--no-update`: A flag to disable updating the file that stores the last picked items.

## Example

### 1. Prepare the Input File

Create an input file (e.g., `data.json`) with the desired data:

```json
[
    { "id": 1, "name": "Item 1" },
    { "id": 2, "name": "Item 2" },
    { "id": 3, "name": "Item 3" },
    { "id": 4, "name": "Item 4" },
    { "id": 5, "name": "Item 5" }
]
```

### 2. Run the Program

Execute the program, specifying the unique `property_name` key (e.g., `id`) and the file where the selected items will be stored (e.g., `last_picks.json`)

```bash
$ python main.py data.json id last_picks.json
```

### 3. View the Output

The program will output a randomly selected item in JSON format:

```json
{
    "status": "success",
    "item": {
        "id": 3,
        "name": "Item 3"
    }
}
```

### 4. Save the Picked Item

The selected item will be saved in the `last_picks.json` file to ensure it won't be picked again:

#### Contents of last_picks.json after the first run:

```json
[{ "id": 3, "name": "Item 3" }]
```

### 5. Repeat Until All Items Are Picked

Run the program again to pick another item, continuing until all items have been picked. The program will manage the selection process to ensure that each item is only picked once.

## Error Codes

Below is a list of possible error codes and their descriptions:

-   `invalid_or_nonexistent_json_file`: Indicates an invalid or non-existent JSON file path.
-   `empty_input_json_file`: Indicates an empty input JSON file.
-   `invalid_property_name`: Indicates an invalid property name provided.
-   `all_items_picked`: Indicates that all items have been picked and no new items are available.
-   `generic_error`: Indicates an unexpected error occurred.

### Example Error Response

```json
{
    "status": "error",
    "message": "Invalid or non-existent JSON file: 'data.json'",
    "error_code": "invalid_or_nonexistent_json_file"
}
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the [MIT License](https://github.com/lucianoayres/rjip/blob/main/LICENSE).
