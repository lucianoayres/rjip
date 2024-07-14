import unittest
import os
import json
import random
from tempfile import NamedTemporaryFile
from rji_cli.json_operations import (
    load_json,
    validate_json_property,
    exclude_json_items_in_common,
    get_random_item,
    all_items_picked,
)

class TestJsonOperations(unittest.TestCase):
    def setUp(self):
        # Initialize test data and resources
        self.data = [{"key": "value"}]
        self.json_data = [
            {"id": 1, "name": "Item 1"},
            {"id": 2, "name": "Item 2"},
            {"id": 3, "name": "Item 3"},
        ]
        self.json1 = [{"id": 1, "name": "Item 1"}, {"id": 2, "name": "Item 2"}]
        self.json2 = [{"id": 1, "name": "Item 1"}]
        self.json3 = [
            {"id": 1, "name": "Item 1"},
            {"id": 2, "name": "Item 2"},
            {"id": 3, "name": "Item 3"},
        ]
        self.json4 = [{"id": 2, "name": "Item 2"}, {"id": 3, "name": "Item 3"}]
        self.temp_files = []  # Initialize an empty list to store temporary file names

    def tearDown(self):
        # Clean up any temporary files created during tests
        for temp_file in self.temp_files:
            os.remove(temp_file)

    def create_temporary_json_file(self, data):
        # Create a temporary JSON file and store its name for cleanup
        temp_file = NamedTemporaryFile(mode="w", delete=False)
        json.dump(data, temp_file)
        temp_file.close()
        self.temp_files.append(temp_file.name)
        return temp_file.name

    def test_load_json(self):
        # Arrange: Create a temporary JSON file with test data
        temp_file_name = self.create_temporary_json_file(self.data)

        # Act: Load JSON data from the temporary file
        loaded_data = load_json(temp_file_name)

        # Assert: Check if loaded data matches the test data
        self.assertEqual(loaded_data, self.data)

    def test_validate_json_property_existing_property(self):
        # Arrange: Create a temporary JSON file with test data
        temp_file_name = self.create_temporary_json_file(self.json_data)

        # Act: Validate an existing property in the JSON file
        result = validate_json_property(temp_file_name, "id")

        # Assert: Check if property validation returns True
        self.assertTrue(result)

    def test_validate_json_property_non_existing_property(self):
        # Arrange: Create a temporary JSON file with test data
        temp_file_name = self.create_temporary_json_file(self.json_data)

        # Act: Validate a non-existing property in the JSON file
        result = validate_json_property(temp_file_name, "non_existing_key")

        # Assert: Check if property validation returns False
        self.assertFalse(result)

    def test_exclude_json_items_in_common(self):
        # Act: Exclude common items between two JSON arrays based on 'id'
        filtered_json = exclude_json_items_in_common(self.json3, self.json4, "id")
        expected_result = [{"id": 1, "name": "Item 1"}]

        # Assert: Check if filtered JSON matches the expected result
        self.assertEqual(filtered_json, expected_result)

    def test_get_random_item(self):
        # Arrange: Set a seed for deterministic randomness
        random.seed(1)

        # Act: Get a random item from JSON data
        random_item = get_random_item(self.json_data)

        # Assert: Check if random item is in the original JSON data
        self.assertIn(random_item, self.json_data)

    def test_get_random_item_empty_data(self):
        # Act & Assert: Ensure ValueError is raised when data is empty
        with self.assertRaises(ValueError):
            get_random_item([])

    def test_all_items_picked_with_items_remaining(self):
        # Act: Check if all items have been picked with items remaining
        result = all_items_picked(self.json_data)

        # Assert: The result should be False
        self.assertFalse(result)

    def test_all_items_picked_with_no_items_remaining(self):
        # Act: Check if all items have been picked with no items remaining
        result = all_items_picked([])

        # Assert: The result should be True
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()

