import time
from threading import Thread
from time import sleep

class Knight(Thread):
    def __init__(self, name, power):
        self.knight_name = name
        self.power = power
        super().__init__()

    def run(self):
        enemies = 100
        days_count = 0
        print(f'{self.knight_name}, на нас напали!')
        while enemies > 0:
            time.sleep(1)
            days_count += 1
            enemies -= self.power
            if enemies > 0:
                print(f'{self.knight_name} сражается {days_count} день(дня)..., '
                      f'осталось {enemies} воинов.')
            else:
                print(f'{self.knight_name} одержал победу спустя {days_count} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
time.sleep(0.1)
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')