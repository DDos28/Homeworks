import threading
import random
from queue import Queue
import time

class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None

class Guest(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        wait_time = random.randint(3, 10)
        print(f"{self.name} сидит за столом и ест. Ожидание: {wait_time} секунд.")
        time.sleep(wait_time)

class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        for guest in guests:
            if any(table.guest is None for table in self.tables):
                for table in self.tables:
                    if table.guest is None:
                        table.guest = guest
                        guest.start()
                        print(f"{guest.name} сел(-а) за стол номер {table.number}")
                        break
            else:
                self.queue.put(guest)
                print(f"{guest.name} в очереди.")

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest is not None and not table.guest.is_alive():
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                    print(f"Стол номер {table.number} свободен")
                    table.guest = None

                    if not self.queue.empty():
                        new_guest = self.queue.get()
                        table.guest = new_guest
                        print(f"{new_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")
                        new_guest.start()

            time.sleep(1)

if __name__ == "__main__":
    table1 = Table(1)
    table2 = Table(2)
    table3 = Table(3)

    cafe = Cafe(table1, table2, table3)  

    guest1 = Guest("Vasya")
    guest2 = Guest("Petya")
    guest3 = Guest("Masha")
    guest4 = Guest("Lena")
    guest5 = Guest("Olga")

    cafe.guest_arrival(guest1, guest2, guest3, guest4, guest5)  # Добавили гостя в список

    cafe.discuss_guests()