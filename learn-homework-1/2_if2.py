"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main(str1, str2):
    if type(str1) != str or type(str2) != str:
        return 0
    elif str1 == str2:
        return 1
    elif len(str1) > len(str2):
        return 2
    elif str1 != str2 and str2 == 'learn':
        return 3
#    elif str1 != str2 and len(str1) == len(str2):
#        return 2.6
#    elif str1 != str2 and len(str1) < len(str2):
#      return 2.5

"""
!!!!  Добавил условие строка 2 длинее первой , вернуло 2.5 
!!!!  Добавил условие длина строк равна , вернуло 2.6
!!!!  Закоментировано, так как нет в ТЗ
"""


    
if __name__ == "__main__":
    print(main(22, 'test'))
    print(main('test', 22))
    print(main(22, 22))
    print(main('test1', 'test1'))
    print(main('test1', 'test2'))
    print(main('test22', 'test2'))
    print(main('test22', 'test222'))
    print(main('test1', 'learn'))
