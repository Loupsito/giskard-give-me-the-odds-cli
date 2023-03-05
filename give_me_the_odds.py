import argparse
import json
from typing import Dict, Any

import requests


def read_json(file_path: str) -> Dict[str, Any]:
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data


def main():
    parser = argparse.ArgumentParser(description='Read 2 JSON files')
    parser.add_argument('file1', type=str, help='path to the first JSON file')
    parser.add_argument('file2', type=str, help='path to the second JSON file')
    args = parser.parse_args()

    millennium_falcon_json = read_json(args.file1)
    empire_json = read_json(args.file2)

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
