import unittest
import os
import json
from rjip.update_operations import update_last_pick_json

class TestUpdateLastPickJson(unittest.TestCase):

    def setUp(self):
        self.json_data = [
            {"id": 1, "name": "Item 1"},
            {"id": 2, "name": "Item 2"},
            {"id": 3, "name": "Item 3"},
        ]
        # Create a temporary file with initial JSON data
        self.temp_file = 'temp_file.json'
        with open(self.temp_file, 'w') as f:
            json.dump(self.json_data, f)

    def tearDown(self):
        # Clean up the temporary file after each test
        if os.path.exists(self.temp_file):
            os.remove(self.temp_file)
    
    def test_update_last_pick_json(self):
        new_item = {"id": 4, "name": "Item 4" }
        update_last_pick_json(self.temp_file, new_item)

        with open(self.temp_file, 'r') as f:
            updated_data = json.load(f)

        expected_data = [
            {"id": 1, "name": "Item 1"},
            {"id": 2, "name": "Item 2"},
            {"id": 3, "name": "Item 3"},
            {"id": 4, "name": "Item 4"}
        ]
        self.assertEqual(updated_data, expected_data)
    
if __name__ == "__main__":
    unittest.main()