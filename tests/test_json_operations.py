import unittest
import os
import json
import random
from tempfile import NamedTemporaryFile
from rji_cli.json_operations import load_json, validate_json_property, exclude_json_items_in_common, get_random_item

class TestJsonOperations(unittest.TestCase):
    def setUp(self):
        self.data = [{"key": "value"}]
        self.json1 = [{"id": 1, "name": "Item 1"}, {"id": 2, "name": "Item 2"}]
        self.json2 = [{"id": 1, "name": "Item 1"}]
        self.json3 = [{"id": 1, "name": "Item 1"}, {"id": 2, "name": "Item 2"}, {"id": 3, "name": "Item 3"}]
        self.json4 = [{"id": 2, "name": "Item 2"}, {"id": 3, "name": "Item 3"}]
        self.json_data = [{"id": 1, "name": "Item 1"}, {"id": 2, "name": "Item 2"}, {"id": 3, "name": "Item 3"}]
    
    def test_load_json(self):
        with NamedTemporaryFile(mode='w',delete=False) as temp_file:
            json.dump(self.data, temp_file)
        loaded_data = load_json(temp_file.name)
        self.assertEqual(loaded_data, self.data)
        os.remove(temp_file.name)

    def test_validate_json_property_existing_property(self):
        with NamedTemporaryFile(mode='w', delete=False) as temp_file:
            json.dump(self.data, temp_file)
            temp_file_name = temp_file.name
        try:
            validate_json_property(temp_file_name, 'key')
        except ValueError:
            self.fail("validate_json_property() raised ValueError unexpectedly!")
        os.remove(temp_file_name)
    
    def test_validate_json_property_non_existing_property(self):
        with NamedTemporaryFile(mode='w', delete=False) as temp_file:
            json.dump(self.data, temp_file)
            temp_file_name = temp_file.name
        with self.assertRaises(ValueError):
            validate_json_property(temp_file_name, 'non_existing_key')
        os.remove(temp_file_name)

    def test_exclude_json_items_in_common(self):
        filtered_json = exclude_json_items_in_common(self.json3, self.json4, 'id')
        expected_result = [{"id": 1, "name": "Item 1"}]
        self.assertEqual(filtered_json, expected_result)

    def test_get_random_item(self):
        random.seed(1)
        random_item = get_random_item(self.json_data)
        self.assertIn(random_item, self.json_data)

    def test_get_random_item_empty_data(self):
        with self.assertRaises(ValueError):
            get_random_item([])
    
if __name__ == '__main__':
    unittest.main()