import unittest
from unittest.mock import patch
from io import StringIO
import json
from rji_cli.utils import print_message, exit_with_message, print_json

class TestUtils(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_message(self, mock_stdout):
        # Arrange
        message = "Hello, world!"
        
        # Act
        print_message(message)
        
        # Assert
        self.assertEqual(mock_stdout.getvalue(), message + '\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test_exit_with_message_default_code(self, mock_stdout):
        # Arrange
        message = "Exiting with default code"
        
        # Act & Assert
        with self.assertRaises(SystemExit) as cm:
            exit_with_message(message)
        
        self.assertEqual(mock_stdout.getvalue(), message + '\n')
        self.assertEqual(cm.exception.code, 0)

    @patch('sys.stdout', new_callable=StringIO)
    def test_exit_with_message_custom_code(self, mock_stdout):
        # Arrange
        message = "Exiting with custom code"
        code = 2
        
        # Act & Assert
        with self.assertRaises(SystemExit) as cm:
            exit_with_message(message, code)
        
        self.assertEqual(mock_stdout.getvalue(), message + '\n')
        self.assertEqual(cm.exception.code, code)

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
