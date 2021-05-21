"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
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


if __name__ == "__main__":
    main(grades)
