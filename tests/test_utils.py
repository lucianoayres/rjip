import unittest
from unittest.mock import patch
from io import StringIO
import json
from rji_cli.utils import print_json

class TestUtils(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_json(self, mock_stdout):
        # Arrange
        data = {"key": "value"}
        expected_output = json.dumps(data) + '\n'
        
        # Act
        print_json(data)
        
        # Assert
        self.assertEqual(mock_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
