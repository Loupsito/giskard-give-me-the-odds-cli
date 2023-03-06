import argparse
import json
from typing import Dict, Any

import requests


def read_json(file_path: str) -> Dict[str, Any]:
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data


def main():
    parser = argparse.ArgumentParser(
        description='Gives the Millennium Falcon ship\'s odds of success in completing its mission')
    parser.add_argument('millennium_falcon', type=str, help='Path to the millennium_falcon.json file')
    parser.add_argument('empire', type=str, help='Path to the empire.json file')
    args = parser.parse_args()

    millennium_falcon_json = read_json(args.millennium_falcon)
    empire_json = read_json(args.empire)

    url = "http://localhost:8000/give_me_the_odds"
    body = {
        "millennium_falcon": millennium_falcon_json,
        "empire": empire_json
    }

    response = requests.post(url, json=body)
    result = response.json()['value']
    print(result)


if __name__ == '__main__':
    main()
