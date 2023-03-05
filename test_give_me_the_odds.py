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
            json.dump({
                "autonomy": 6,
                "departure": "Tatooine",
                "arrival": "Endor",
                "routes_db": "universe.db"
            }, f)
        with open(self.file2, 'w') as f:
            json.dump({
                "countdown": 8,
                "bounty_hunters": [
                    {
                        "planet": "Hoth",
                        "day": 6
                    },
                    {
                        "planet": "Hoth",
                        "day": 7
                    },
                    {
                        "planet": "Hoth",
                        "day": 8
                    }
                ]
            }, f)

    def tearDown(self):
        os.remove(self.file1)
        os.remove(self.file2)

    def test_read_json(self):
        data = read_json(self.file1)
        self.assertEqual(data, {
            "autonomy": 6,
            "departure": "Tatooine",
            "arrival": "Endor",
            "routes_db": "universe.db"
        })

    @patch('requests.post')
    def test_main(self, mock_post):
        mock_post.return_value.json.return_value = {"value": 81.0}
        captured_output = io.StringIO()
        args = [self.file1, self.file2]

        with patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(file1=args[0], file2=args[1])):
            with contextlib.redirect_stdout(captured_output):
                main()

        expected_output = "81.0\n"
        self.assertEqual(expected_output, captured_output.getvalue())


if __name__ == '__main__':
    unittest.main()
