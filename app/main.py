"""Генератор приветствий."""
import pprint


def greeting(name: str) -> str:
    """Возвращает текст приветствия.

    Args:
        name: Имя пользователя

    Returns:
        str: Текст приветствия
    """
    if not isinstance(name, str):
        name = str(name)
    single_word_list = name.split()
    if len(single_word_list) > 1:
        temp_valid_name_list = []
        for word in single_word_list:
            temp_valid_name_list.append(word.capitalize())
        name = ' '.join(temp_valid_name_list)
    else:
        name = name.capitalize()
    pp = pprint.PrettyPrinter()
    pp.pprint(name.lower())
    return 'Привет, {name}'.format(name=name)
