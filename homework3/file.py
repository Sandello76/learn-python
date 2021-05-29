"""
Скачайте файл по ссылке
Прочитайте содержимое файла в переменную, подсчитайте длину получившейся строки
Подсчитайте количество слов в тексте
Замените точки в тексте на восклицательные знаки
Сохраните результат в файл referat2.txt
"""
import wget
import os.path

try:
    check_file = os.path.exists('./referat.txt')
except FileNotFoundError:
    print('Файл не существует!')

if check_file == False:
    wget.download('https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0')
else:
    print("Файл уже скачан")


def main():
    with open('referat.txt', 'r', encoding='utf-8') as f:
        read = f.read()
        print(len(read.split()))
        print(len(read))
        write = read.replace('.', '!')
        with open('referat2.txt', 'w', encoding='utf-8') as new:
            new.write(write)


if __name__ == "__main__":
    main()
