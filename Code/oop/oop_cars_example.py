# auto v = 90-120
#km/h - random
# 10 db
# 10 h
# sum km / aut
import random


class Auto:

    speed_treshold = (90, 120)

    def __init__(self, len_runned=0):
        self.actual_speed = 0
        self.len_runned = len_runned
        self.type = self.get_type()

    def get_type(self):
        return "Auto"

    def set_actual_speed(self):
        self.actual_speed = random.randint(
            self.speed_treshold[0], self.speed_treshold[1])

    def set_len_runned(self):
        self.len_runned += self.actual_speed

    def p(self):
        print("brum-brum")


class Truck(Auto):

    speed_treshold = (100, 100)

    def get_type(self):
        return "Truck"

    # def set_actual_speed(self):
    #self.actual_speed = 100


class Motorcycle(Auto):

    speed_treshold = (60, 120)

    def __init__(self):
        super().__init__(10)

    def get_type(self):
        return "Motorcycle"


def main():

    # Auto().p()

    a = Auto()

    # a.p()

    autos = []

    for i in range(4):
        autos.append(Auto())

    for i in range(4):
        autos.append(Truck())

    for i in range(2):
        autos.append(Motorcycle())

    for i in range(10):
        for i in range(10):
            autos[i].set_actual_speed()
            autos[i].set_len_runned()

    for i in range(10):
        print(str(autos[i].len_runned) + autos[i].type)

main()
