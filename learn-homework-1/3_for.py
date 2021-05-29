"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.

!!!! Переделал с использованием https://docs.python.org/3/library/statistics.html#statistics.mean !!!!
"""
grades = [
    {'school_class': '4a', 'scores': [3, 4, 3, 5, 2]},
    {'school_class': '4b', 'scores': [1, 2, 3, 4, 5]},
    {'school_class': '4c', 'scores': [5, 4, 4, 2, 2]}
]


def main(grades):

    grades_class = {}
    all_school = 0

    for school_class in grades:
        class_grade = round(sum(school_class['scores']) / len(school_class["scores"]), 1)
        grades_class[school_class['school_class']] = class_grade
        all_school += sum(school_class['scores'])

    mid_grade = round(all_school / (len(grades) * len(grades[0]['scores'])), 1)

    print(f"средний балл по всей школе : {mid_grade}")

    for school_class, grade in grades_class.items():
        print(f"редний балл по каждому классу {school_class} ' = ' {grade}")



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
