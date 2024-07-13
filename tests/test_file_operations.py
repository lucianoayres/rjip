import unittest
import os
from rji_cli.file_operations import file_exists

class TestFileOperations(unittest.TestCase):

    def setUp(self):
        # Create any necessary resources or setup steps here
        pass

    def tearDown(self):
        # Clean up any resources after each test method runs
        if os.path.exists('test_file.json'):
            os.remove('test_file.json')

    def test_file_exists_with_existing_file(self):
        # Arrange: Create a test file
        with open('test_file.json', 'w') as f:
            f.write('{"key": "value"}')

        # Act & Assert: Check if the file exists
        self.assertTrue(file_exists('test_file.json'))

    def test_file_exists_with_non_existing_file(self):
        # Act & Assert: Check if the file does not exist
        self.assertFalse(file_exists('non_existing_file.json'))

if __name__ == '__main__':
    unittest.main()
