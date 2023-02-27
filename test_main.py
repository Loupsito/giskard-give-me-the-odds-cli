import argparse
import contextlib
import io
import json
import os
import unittest
from unittest.mock import patch

from give_me_the_odds import read_json, main


class TestReadJson(unittest.TestCase):

    def setUp(self):
        self.test_dir = os.path.dirname(os.path.abspath(__file__))
        self.file1 = os.path.join(self.test_dir, 'test_file1.json')
        self.file2 = os.path.join(self.test_dir, 'test_file2.json')

        with open(self.file1, 'w') as f:
            json.dump({'a': 1, 'b': 2}, f)
        with open(self.file2, 'w') as f:
            json.dump({'c': 3, 'd': 4}, f)

    def tearDown(self):
        os.remove(self.file1)
        os.remove(self.file2)

    def test_read_json(self):
        data = read_json(self.file1)
        self.assertEqual(data, {'a': 1, 'b': 2})

    def test_main(self):
        captured_output = io.StringIO()
        args = [self.file1, self.file2]

        with patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(file1=args[0], file2=args[1])):
            with contextlib.redirect_stdout(captured_output):
                main()

        expected_output = "{'a': 1, 'b': 2}\n{'c': 3, 'd': 4}\n"
        self.assertEqual(expected_output, captured_output.getvalue())


if __name__ == '__main__':
    unittest.main()
