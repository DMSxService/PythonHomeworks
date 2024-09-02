from time import sleep
from datetime import datetime
from threading import Thread

time_start = datetime.now()


def wite_words(word_count, file_name):
    for i in range(1, word_count + 1):
        with open(file_name, 'a', encoding='utf-8') as strings:
            strings.write(f'Какое-то слово № {i}' + '\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')

time_end = datetime.now()
time_res = time_end - time_start
print(f'Работа функций {time_res}')

time_start = datetime.now()
F5 = Thread(target=wite_words, args=(10, 'example5.txt'))
F6 = Thread(target=wite_words, args=(30, 'example6.txt'))
F7 = Thread(target=wite_words, args=(200, 'example7.txt'))
F8 = Thread(target=wite_words, args=(100, 'example8.txt'))
F5.start()
F6.start()
F7.start()
F8.start()
F5.join()
F6.join()
F7.join()
F8.join()
time_end = datetime.now()
time_res = time_end - time_start
print(f'Работа потоков {time_res}')
