import time
from time import sleep
from threading import Thread

time_start = time.time()
def wite_words(word_count, file_name):
    with open(file_name, "w", encoding='utf-8') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово № {i + 1}\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')

wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')

time_end = time.time()
print(f'Работа потоков {time_end - time_start}')
print()

time_start = time.time() # Взятие текущего времени

thread_1 = Thread(target=wite_words, args=(10, 'example5.txt'))
thread_2 = Thread(target=wite_words, args=(30, 'example6.txt'))
thread_3 = Thread(target=wite_words, args=(200, 'example7.txt'))
thread_4 = Thread(target=wite_words, args=(100, 'example8.txt'))

thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()

thread_1.join()
thread_2.join()
thread_3.join()
thread_4.join()

time_end = time.time()
print(f'Работа потоков {time_end - time_start}')