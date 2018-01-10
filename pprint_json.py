import json
import sys


def load_data(file_path):
    try:
        with open(file_path, 'r') as file_handler:
            return json.load(file_handler)
    except OSError:
        return False


def pretty_print_json(json_str):
    return json.dumps(json_str, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Не указан файл')
        sys.exit()

    input_file_path = sys.argv[1]
    no_pretty_json = load_data(input_file_path)
    if no_pretty_json:
        print(pretty_print_json(no_pretty_json))
    else:
        print("Не могу прочитать файл", input_file_path)
