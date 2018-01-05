import json
import sys


def load_data(filepath):
    with open(filepath, 'r') as file_handler:
        return json.load(file_handler)


def pretty_print_json(deserializesjson):
    return json.dumps(deserializesjson, skipkeys=False, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    filepath = sys.argv[1]
    deserializesjson = load_data(filepath)
    if (deserializesjson):
        print (pretty_print_json(deserializesjson))
