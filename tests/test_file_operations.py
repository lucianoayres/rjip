import unittest
import os
from json_random_item_picker import file_exists

class TestFileOperations(unittest.TestCase):

    def test_file_exists_existing_file(self):
        with open('test_file.json', 'w') as f:
            f.write('{"key": "value"}')
        self.assertTrue(file_exists('test_file.json'))
        os.remove('test_file.json')
    
    def test_file_exists_non_existing_file(self):
        self.assertFalse(file_exists('non_existing_file.json'))

if __name__ == '__main__':
    unittest.main()