import itertools


def open_files(path: str):
    """Открытие файла"""
    try:
        with open(path, encoding='utf-8') as f:
            data_begin = f.readlines()
            data_fin = [i.strip() for i in data_begin if len(i.strip()) > 0]
        return data_fin
    except FileNotFoundError:
        print('файл не найден')


def get_commands(command, value, data):
    """Работаем с командами"""
    if command == 'filter':
        res = filter(lambda x: value in x, data)
    elif command == 'map':
        res = map(lambda x: x.split()[int(value)], data)
    elif command == 'unique':
        res = set(data)
    elif command == 'sort':
        res = sorted(data) if value == 'asc' else sorted(data, reverse=True)
    elif command == 'limit':
        res = itertools.islice(data, int(value))

    return res
