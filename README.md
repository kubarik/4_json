# Форматирование json

Вывод JSON содержимое в консоль в удобном для чтения виде: добавляет переносы строк, отступы слева и пробелы.

# Как использовать

Импортируемые модули
```python
import json #кодирование и декодирование данных
import sys #доступ к переменным
```

Сначала получаем десериализацию JSON, с помощью функции:
```python
load_data(file_path)
```
где
  file_path - путь до файла с произвольными данными в формате JSON.

В случае успеха, выполняется функция преобразования JSON в читаемый удобный вид:
```python
pretty_print_json(deserializes_json_obj)
```
где
  deserializes_json_obj - JSON, загруженный из файла.

```bash

Входный данные
{"name":"John","age":30,"cars":[ "Ford","BMW","Fiat"]}
```

```bash

Запус и ответ
$ python pprint_json.py <path to file>
{
    "name": "John",
    "age": 30,
    "cars": [
        "Ford",
        "BMW",
        "Fiat"
    ]
}
```

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке ― [DEVMAN.org](https://devman.org)
