import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.power = power

    def run(self):
        day = 0
        bots = 100
        print(f'{self.name}, на нас напали!')
        while bots != 0:
            day += 1
            bots -= self.power
            print(f'{self.name}, сражается {day} день(дня)..., осталось {bots} воинов', flush=True)
            time.sleep(1)
        print(f'{self.name} одержал победу спустя {day} дней!')


knight1 = Knight("Sir Lancelot", 10)
knight2 = Knight("Sir Galahad", 20) 
knight1.start()
knight2.start()
knight1.join()
knight2.join()
print(f'Все битвы закончились!')
