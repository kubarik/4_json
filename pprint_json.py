import json
import sys


def load_data(filepath):
    try:
        file_handler = open(filepath, 'r')
        try:
            return json.load(open(filepath))
        finally:
            file_handler.close()
    except OSError as ex:
        print("Не могу прочитать файл", filepath, ": Ошибка ", ex)

def pretty_print_json(deserializes_json):
    return json.dumps(deserializes_json, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print ('Не указан файл')
        sys.exit()

    filepath = sys.argv[1]
    deserializes_json = load_data(filepath)
    if deserializes_json:
        print (pretty_print_json(deserializes_json))
