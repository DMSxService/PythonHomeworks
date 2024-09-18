import queue
from threading import Thread
from random import randint
from time import sleep

tr_list = []


class Table:

    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        waiting = randint(3, 10)
        for i in range(waiting):
            sleep(1)


class Cafe:
    q = queue.Queue()
    global tr_list

    def __init__(self, *args):
        self.tables = args

    def guest_arrival(self, *guests):
        t3 = list(guests)
        while len(tables) and len(t3):
            t1 = tables.pop(0)
            t2 = t3.pop(0)
            if t1.guest is None:
                t1.guest = t2.name
                tables.append(t1)
                t4 = Guest(t1.guest)
                t4.start()
                tr_list.append(t4)
                print(f'{t2.name} сел(-а) за стол номер {t1.number}')
            else:
                self.q.put(t2.name)
                print(f'{t2.name} в очереди')
                tables.append(t1)
        return

    def discuss_guests(self):
        while len(tr_list):
            t4 = tr_list.pop(0)
            t5 = t4.is_alive()
            if not t5:
                t1 = tables.pop(0)
                t2 = t1.number
                t3 = t1.guest
                print(f'{t3}  покушал(-а) и ушёл(ушла)')
                t1.guest = None
                print(f'Стол номер {t2} свободен')

                if not self.q.empty():
                    tables.insert(0, t1)
                    t3 = self.q.get()
                    self.guest_arrival(Guest(t3))
                else:
                    continue
            else:
                tr_list.append(t4)



# Создание столов
tables = [Table(number) for number in range(1, 6)]

# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]

# Заполнение кафе столами
cafe = Cafe(*tables)

# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
