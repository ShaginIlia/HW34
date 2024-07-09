from threading import Thread
import time


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = str(name)
        self.power = int(power)
        self.enemy = 100

    def run(self):
        days = 0
        print(f'{self.name}, на нас напали!')
        while self.enemy > 0:
            self.enemy -= self.power
            days += 1
            print(f'{self.name} сражается {days} день(дней), осталось {self.enemy} воинов.')
            time.sleep(1)
        print(f'{self.name} одержал победу спустя <кол-во дней> дней(дня)!')


my_knight = Knight('Mike', 10)
my_knight2 = Knight('Loe', 5)
my_knight3 = Knight('Vincent', 13)
my_knight.start()
my_knight.join()
my_knight2.start()
my_knight2.join()
my_knight3.start()
my_knight3.join()
