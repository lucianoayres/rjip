import unittest
import os
import json
from unittest.mock import patch, mock_open
from rjip.file_operations import (
    file_exists,
    resolve_last_pick_file_path,
    create_empty_json_file,
    is_json_valid
)

class TestFileOperations(unittest.TestCase):

    def setUp(self):
        # Create any necessary resources or setup steps here
        pass

    def tearDown(self):
        # Clean up any resources after each test method runs
        files_to_remove = [
            'test_file.json', 'last_pick_custom.json',
            'last_pick_input_file.json', 'last_pick_another_input_file.json',
            'existing_file.json', 'io_error_file.json',  # Ensure consistency in file names
            'test.json',  # Added cleanup for test.json used in is_json_valid tests
            'io_error.json'  # Added cleanup for io_error.json used in is_json_valid tests
        ]
        for file in files_to_remove:
            if os.path.exists(file):
                os.remove(file)

    def test_file_exists_with_existing_file(self):
        # Arrange: Create a test file
        with open('test_file.json', 'w') as f:
            f.write('{"key": "value"}')

        # Act & Assert: Check if the file exists
        self.assertTrue(file_exists('test_file.json'))

    def test_file_exists_with_non_existing_file(self):
        # Act & Assert: Check if the file does not exist
        self.assertFalse(file_exists('non_existing_file.json'))

    def test_file_exists_with_invalid_path(self):
        # Act & Assert: Check if invalid path raises an error
        with self.assertRaises(TypeError):
            file_exists(None)

    def test_resolve_last_pick_file_path_with_last_pick_file(self):
        # Act: Call the function with a last_pick_file provided
        result = resolve_last_pick_file_path('input_file.json', 'last_pick_custom.json')

        # Assert: The result should be the provided last_pick_file
        self.assertEqual(result, 'last_pick_custom.json')

    def test_resolve_last_pick_file_path_without_last_pick_file(self):
        # Act: Call the function without a last_pick_file provided
        result = resolve_last_pick_file_path('input_file.json')

        # Assert: The result should be the generated last_pick file name
        self.assertEqual(result, 'last_pick_input_file.json')

    def test_resolve_last_pick_file_path_with_different_input_file(self):
        # Act: Call the function with a different input file name
        result = resolve_last_pick_file_path('another_input_file.json')

        # Assert: The result should be the generated last_pick file name based on the input file
        self.assertEqual(result, 'last_pick_another_input_file.json')

    def test_create_empty_json_file(self):
        # Arrange: Define the test file path
        test_file_path = 'test_file.json'

        # Act: Call the function to create an empty JSON file
        create_empty_json_file(test_file_path)

        # Assert: Check if the file exists and is empty JSON
        self.assertTrue(file_exists(test_file_path))
        with open(test_file_path, 'r') as file:
            data = json.load(file)
            self.assertEqual(data, [])

    def test_create_empty_json_file_existing_file(self):
        # Arrange: Create a mock for an existing file
        existing_file_path = 'existing_file.json'
        with open(existing_file_path, 'w') as f:
            f.write('{"existing": true}')

        # Act: Call the function to create an empty JSON file over an existing file
        create_empty_json_file(existing_file_path)

        # Assert: Check if the existing file content is overwritten and now empty
        self.assertTrue(file_exists(existing_file_path))
        with open(existing_file_path, 'r') as file:
            data = json.load(file)
            self.assertEqual(data, [])

    def test_is_json_valid_existing_file_valid_json(self):
        # Arrange: Create a mock for opening the file with valid JSON
        file_path = 'test.json'
        mock_open_func = mock_open(read_data='{"key": "value"}')

        # Act & Assert: Use patch to mock open function and test is_json_valid
        with patch('builtins.open', mock_open_func):
            valid = is_json_valid(file_path)
            self.assertTrue(valid)

    def test_is_json_valid_existing_file_invalid_json(self):
        # Arrange: Create a mock for opening the file with invalid JSON
        file_path = 'test.json'
        mock_open_func = mock_open(read_data='{"key": "value"')  # Invalid JSON missing closing brace

        # Act & Assert: Use patch to mock open function and test is_json_valid
        with patch('builtins.open', mock_open_func):
            valid = is_json_valid(file_path)
            self.assertFalse(valid)

    def test_is_json_valid_non_existing_file(self):
        # Act & Assert: Test with a non-existing file
        file_path = 'non_existing.json'
        valid = is_json_valid(file_path)
        self.assertFalse(valid)

    def test_is_json_valid_invalid_file_path(self):
        # Act & Assert: Test with invalid file path
        with self.assertRaises(TypeError):
            is_json_valid(None)

if __name__ == '__main__':
    unittest.main()
