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
        self.millennium_falcon = os.path.join(self.test_dir, 'test_millennium_falcon.json')
        self.empire = os.path.join(self.test_dir, 'test_empire.json')

        with open(self.millennium_falcon, 'w') as f:
            json.dump({
                "autonomy": 6,
                "departure": "Tatooine",
                "arrival": "Endor",
                "routes_db": "universe.db"
            }, f)
        with open(self.empire, 'w') as f:
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
        os.remove(self.millennium_falcon)
        os.remove(self.empire)

    def test_read_json(self):
        data = read_json(self.millennium_falcon)
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
        args = [self.millennium_falcon, self.empire]

        with patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(millennium_falcon=args[0], empire=args[1])):
            with contextlib.redirect_stdout(captured_output):
                main()

        expected_output = "81.0\n"
        self.assertEqual(expected_output, captured_output.getvalue())


if __name__ == '__main__':
    unittest.main()
