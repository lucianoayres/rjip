![rJip_logo](https://github.com/user-attachments/assets/cc0c916c-ca2f-4345-9b98-739d666e34a4)

# rJip: Random JSON Item Picker

Command-line tool designed to pick a random item from a JSON file while ensuring that each item is picked only once. It keeps track of previously picked items to maintain uniqueness until all items have been picked at least once.

![rjip_demo](https://github.com/user-attachments/assets/b95c8c24-833f-472a-a0b9-831c55aa5ab0)

## Features

-   Random Item Selection: Retrieves a random item from a specified JSON file.
-   Tracking Last Picks: Maintains a record of previously picked items to avoid duplicates.
-   Property Validation: Validates a specified property name within the JSON data.
-   Error Handling: Includes specific error codes for different validation and operational errors.

## Usage

To use the tool, execute `rjip` binary file in the `dist` directory with the following parameters:

```bash
$ ./rjip [input_file] [property_name] [last_pick_file] [--no-update]
```

### Arguments

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

## Development

If you want to build and collaborate on the project, follow these steps to set up your development environment.

### 1. Setting Up the Virtual Environment

First, create the virtual environment:

```bash
make venv
```

### 2. Installing Dependencies

First, make sure to activate the virtual environment:

```bash
source venv/bin/activate
```

Then, install the development dependencies listed in the `requirements-dev.txt` file:

```bash
make install-deps
```

The `requirements-dev.txt` file includes:

-   [pytest](https://github.com/pytest-dev/pytest)
-   [pytest-cov](https://github.com/pytest-dev/pytest-cov)
-   [coverage](https://github.com/nedbat/coveragepy)

### 3. Running tests

To run tests using `pytest`:

```bash
make test
```

To run tests using `unittest`:

```bash
make test-unittest
```

### 4. Generating Coverage Reports

To run coverage tests and generate a report:

```bash
make coverage
```

To generate an HTML coverage report:

```bash
make coverage-report
```

### 5. Building

To build the binary file:

```bash
make build
```

### 5. Cleaning Up

First, exit the virtual environment:

```bash
deactivate
```

Then clean up the virtual environment and coverage files

```bash
make clean
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the [MIT License](https://github.com/lucianoayres/rjip/blob/main/LICENSE).
