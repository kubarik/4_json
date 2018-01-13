import json
import sys


def load_data(file_path):
    try:
        with open(file_path, 'r') as file_handler:
            return json.load(file_handler)
    except OSError:
        return False


def pretty_print_json(deserializes_json_obj):
    return json.dumps(deserializes_json_obj, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('Не указан файл')

    input_file_path = sys.argv[1]
    deserializes_json = load_data(input_file_path)
    if response:
        print(pretty_print_json(deserializes_json))
    else:
        print("Не могу прочитать файл", input_file_path)
