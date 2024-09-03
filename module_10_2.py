from time import sleep
from datetime import datetime
from threading import Thread


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        warriors = 100
        days = int(warriors / self.power)
        for i in range(days):
            warriors -= self.power
            print(f'{self.name} сражается {i + 1}..., осталось {warriors} воинов.', end='\n')
            sleep(1)
        print(f'{self.name} одержал победу спустя {days} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
print('Все битвы закончились!')
