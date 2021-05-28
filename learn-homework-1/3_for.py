"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.

!!!! Переделал с использованием https://docs.python.org/3/library/statistics.html#statistics.mean !!!!
"""

import statistics
def main():

    grades = [
    {'school_class': '4a', 'scores': [1, 2, 3, 4]},
    {'school_class': '4b', 'scores': [5, 4, 3, 2, 1]},
    {'school_class': '4c', 'scores': [4, 3, 5]},
    {'school_class': '4e', 'scores': [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]}
    ]


    all_school = []

    for i in range(len(grades)):
        grades_class = (grades[i])
        cl = statistics.mean(grades_class['scores'])
        i = i + 1
        all_school.extend(grades_class['scores'])
        med = round(statistics.mean(all_school), 1)
        print("Средний балл по классу ",grades_class['school_class'], med)

    print(f"Cредний балл по всей школе = {med}")

if __name__ == "__main__":
   main()
