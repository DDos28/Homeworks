from time import sleep
from datetime import datetime
from threading import Thread

time_start = datetime.now()

def wite_words(word_count, file_name):
    with open(file_name, mode='w', encoding='UTF-8') as file:
        for i in range(1, word_count + 1):
            file.write(f'Какое-то слово № {i}'+'\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')

wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')

time_end = datetime.now()
time_res = time_end - time_start
print(time_res)

time_start1 = datetime.now()

thr_first = Thread(target=wite_words, args=(10, 'example5.txt'))
thr_second = Thread(target=wite_words, args=(30, 'example6.txt'))
thr_third = Thread(target=wite_words, args=(200, 'example7.txt'))
thr_fourth = Thread(target=wite_words, args=(100, 'example8.txt'))

thr_first.start()
thr_second.start()
thr_third.start()
thr_fourth.start()

thr_first.join()
thr_second.join()
thr_third.join()
thr_fourth.join()

time_end1 = datetime.now()
time_res1 = time_end1 - time_start1
print(time_res1)

