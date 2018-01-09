# Форматирование json

Вывод JSON содержимое в консоль в удобном для чтения виде: добавляет переносы строк, отступы слева и пробелы.

# Как использовать

Сначала получаем десериализацию JSON, с помощью функции:
```python
load_data(filepath)
```
где
  filepath - путь до файла с произвольными данными в формате JSON.

В случае успеха, выполняется функция преобразования JSON в читаемый удобный вид:
```python
pretty_print_json(deserializes_json)
```
где
  deserializes_json - JSON, загруженный из файла.

Импортируемые модули
```python
import json #кодирование и декодирование данных
import sys #доступ к переменным
```

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
