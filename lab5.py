import re
import csv

def first_exercise():
    file1 = open('task1-en.txt', 'r', encoding='utf-8').read()

    picters = re.findall(r"рис. \w+|Fig. \w+", file1)
    words4 = re.findall(r'\b[a-zA-Z]{4}\b', file1)

    print(f'\n"рис."  или "Fig.":\n {picters}')
    print(f'\nCлова из 4 букв: \n{words4}')

def second_exercise():
    file2 = open('task2.html', 'r', encoding='utf-8').read()

    font_style = re.findall(r'font-style: \w+', file2)
    font_size = re.findall(r'font-weight: \w+', file2)

    for i in range(len(font_style)):
        print(f'{font_style[i]}, {font_size[i]}')

def third_exercise():
    file3 = open('task3.txt', 'r', encoding='utf-8').read()

    output = open('users.csv', 'w')
    output.write(f'ID, Surname, Email, Registration Date, Site\n')

    name = re.findall(r'[A-Z][a-z]+', file3)
    mail = re.findall(r'\w+@\w+.\w+', file3)
    date = re.findall(r'\d{4}-\d\d-\d\d', file3)
    site = re.findall(r'https?://[\w.-]+/', file3)

    for i in range(len(name)):
        output.write(f'{i+1}, {name[i]}, {mail[i]}, {date[i]}, {site[i]}\n')

    output.close()
    print(f'\nВ файл users.scv записаны пользователи в корректном формате.')

def additional_exercise():
    file = open('task_add.txt', 'r', encoding='utf-8').read()

    dates = re.findall(r'\b(\d{2,4}[-/.]+\d{2,4}[-/.]+\d{2,4})', file)
    emails = re.findall(r'\s(\w+@\w+\.[a-zA-Z]{2,})', file)
    sites = re.findall(r'\b(https?://[\w.-]+)', file)

    print(f'\nДаты: {dates}')
    print(f'Почты: {emails}')
    print(f'Сайты: {sites}')

if __name__ == "__main__":
    first_exercise()

    print(f'\n')
    second_exercise()

    third_exercise()

    additional_exercise()
