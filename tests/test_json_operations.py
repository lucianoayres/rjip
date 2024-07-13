import json
import unittest
import os
from tempfile import NamedTemporaryFile
from test_json_operations import load_json, validate_json_property, exclude_json_items_in_common, get_random_item

class TestJsonOperations(unittest.TestCase):
    def setUp(self):
        self.json1 = [{"id": 1, "name": "Item 1"}, {"id": 2, "name": "Item 2"}]
        self.json2 = [{"id": 1, "name": "Item 1"}]
    
    def test_load_json(self):
        data = [{"key": "value"}]
        with NamedTemporaryFile(delete=False) as temp_file:
            json.dump(data, temp_file)
        loaded_data = load_json(temp_file.name)
        self.asserEqual(loaded_data, data)
        os.remove(temp_file.name)