import threading
from threading import Thread, Lock
import time
import random

class Bank:

    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self, i):
        self.balance += i
        print(f"Пополнение: {i}. Баланс: {self.balance}")
        if self.balance >= 500 and self.lock.locked():
            self.lock.release()
        time.sleep(0.001)

    def take(self, i):
        print(f'Запрос на {i}')
        if i < self.balance:
            self.balance -= i
            print(f"Снятие: {i}. Баланс: {self.balance}")
        else:
            print(f'Запрос отклонён, недостаточно средств')
            self.lock.acquire()

bk = Bank()
for i in range(100):
    bk.deposit(random.randint(50, 500))
threads = [threading.Thread(target=bk.take, args=(random.randint(50, 500),)) for _ in range(100)]

[t.start() for t in threads]

for thread in threads:
    thread.join()

print(f'Итоговый баланс: {bk.balance}')