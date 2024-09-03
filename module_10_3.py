from time import sleep
from threading import Thread, Lock
from random import randint


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            if (self.balance >= 500) and self.lock.locked():
                self.lock.release()
            else:
                income = randint(50, 500)
                self.balance += income
                print(f'Пополнение: {income}. Баланс: {self.balance}', end='\n')
            sleep(0.1)

    def take(self):
        for i in range(100):
            expense = randint(50, 500)
            print(f'Запрос: {expense}', end='\n')
            if expense <= self.balance:
                self.balance -= expense
                print(f'Снятие: {expense}. Баланс: {self.balance}', end='\n')
            else:
                print('Запрос отклонён, недостаточно средств', end='\n')
                self.lock.acquire()


bk = Bank()
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
