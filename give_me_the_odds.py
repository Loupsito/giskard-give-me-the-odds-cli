import argparse
import json
from typing import Dict, Any


def read_json(file_path: str) -> Dict[str, Any]:
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data


def main():
    parser = argparse.ArgumentParser(description='Read 2 JSON files')

    parser.add_argument('file1', type=str, help='path to the first JSON file')
    parser.add_argument('file2', type=str, help='path to the second JSON file')

    args = parser.parse_args()

    json1 = read_json(args.file1)
    json2 = read_json(args.file2)

    print(json1)
    print(json2)


if __name__ == '__main__':
    main()
