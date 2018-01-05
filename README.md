# Prettify JSON

Вывод JSON содержимое в консоль в удобном для чтения виде: добавляет переносы строк, отступы слева и пробелы.

# Quickstart

Сначала получаем десериализацию JSON, с помощью функции:
```python
load_data(filepath)
```
где
  filepath - путь до файла с произвольными данными в формате JSON.

В случае успеха, выполняется функция преобразования JSON в читаемый удобный вид:
```python
pretty_print_json(data)
```
где
  data - JSON, загруженный из файла.


```bash

Входный данные
{"name":"John","age":30,"cars":[ "Ford","BMW","Fiat"]}
```

```bash

Ответ
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

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
