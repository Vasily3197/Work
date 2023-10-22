# -*- coding: utf-8 -*import


import Note


def create_note(number):
    title = check_len_text_input(
        input('Введите название Вашей заметки: '), number)
    body = check_len_text_input(
        input('Введите описание Вашей заметки: '), number)
    return Note.Note(title=title, body=body)


def menu():
    print("Выберете нужное:\n\n1 - Вывод всех заметок из файла\n2 - Добавление заметки\n3 - Удаление\n4 - Редактирование\n5 - Выбор по дате\n6 - Выбор по id\n7 - Выход\n")


def check_len_text_input(text, n):
    while len(text) <= n:
        print(f'Текст должен быть больше {n} символов\n')
        text = input('Введите тескт: ')
    else:
        return text


def goodbuy():
    print("До свидания!")