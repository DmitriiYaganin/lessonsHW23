import itertools
import re
from typing import List, Set, Any, Optional


def open_files(path: str) -> List[str]:
    """Открытие файла"""
    try:
        with open(path, encoding='utf-8') as f:
            data_begin = f.readlines()
            data_fin = [i.strip() for i in data_begin if len(i.strip()) > 0]
        return data_fin
    except FileNotFoundError:
        print('файл не найден')


def get_commands(command: str, value, data: list) -> List:
    """Работаем с командами"""
    if command == 'filter':
        res = list(filter(lambda x: value in x, data))
    elif command == 'map':
        res = list(map(lambda x: x.split()[int(value)], data))
    elif command == 'unique':
        res = list(set(data))
    elif command == 'sort':
        res = list(sorted(data) if value == 'asc' else sorted(data, reverse=True))
    elif command == 'limit':
        res = list(itertools.islice(data, int(value)))
    elif command == 'regex':
        regex = re.compile(value)
        res = list(filter(lambda x: re.search(regex, x), data))

    return res
