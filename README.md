# Описание 
Скрипт сделан для двух задач: сокращение ссылок и подсчёт переходов по сокращённой ссылке. Для этого используется cервис `bit.ly` и его API.
Основной код написан на `python3`.

### Как установить

Перед началом работы нужен скам `python`. Устанавливаем по [ссылке](https://www.python.org/downloads/release/python-3120/)
Регистрируемся на сайте bit.ly и генерируем `API-токен`
После скачиваем необходимые файлы
Затем используйте `pip` в командной строке для установки зависимостей:
```
pip install -r requirements.txt
```
### Как запустить
Создаём в директории со скачанными файлами файл `.env` c таким содержимым:
```
BITLY_TOKEN = сюда токен
Для получения сокращённой ссылки пишем команду:
```
[Путь к исполняемому файлу]/main.py --url "ccылка"
```
Для получения статистики переходов по сокращённой ссылке пишем в командную строку:
```
[Путь к исполняемому файлу]/main.py --url "cокращённая ccылка"
```
