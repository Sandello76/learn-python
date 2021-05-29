"""
Создайте список словарей:
        [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'},
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'},
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
    ]
Запишите содержимое списка словарей в файл в формате csv
"""
import os.path
import csv

try:
    check_file = os.path.exists('./dict.csv')
except FileNotFoundError:
    print('Файл не существует!')

if check_file == False:
    print('Файла нет - можно создавать')
else:
    print("Файл есть!!! данные могут быть потеряны")


def main():
    user_dict = [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'},
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'},
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
    ]

    with open('dict.csv', 'w', encoding='utf-8', newline='') as f:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(f, fields, delimiter=';')
        writer.writeheader()
        for user in user_dict:
            writer.writerow(user)


if __name__ == "__main__":
    main()
