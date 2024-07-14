import unittest
import os
import json
from rji_cli.file_operations import file_exists, resolve_last_pick_file_path, create_empty_json_file

class TestFileOperations(unittest.TestCase):

    def setUp(self):
        # Create any necessary resources or setup steps here
        pass

    def tearDown(self):
        # Clean up any resources after each test method runs
        files_to_remove = ['test_file.json', 'last_pick_custom.json', 'last_pick_input_file.json', 'last_pick_another_input_file.json']
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

if __name__ == '__main__':
    unittest.main()
