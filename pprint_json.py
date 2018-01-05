import json


def load_data(filepath):
    with open(filepath, 'r') as file_handler:
        return json.load(file_handler)


def pretty_print_json(data):
    return json.dumps(deserializesJson, skipkeys=False, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    deserializesJson = load_data('') # указать путь к файлу
    if (deserializesJson):
        print (pretty_print_json(deserializesJson))
