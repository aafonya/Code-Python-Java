import time


class Dates:

    def __init__(self, y, m, d):
        self.y = y
        self.m = m
        self.d = d

    # the next to classmethods work together as an alternative constructor,
    # which can construct the current date as an instance of the class Date
    # if we call the today method
    @classmethod
    def fromtimestamp(cls, t):
        y, m, d, hh, mm, ss, weekday, jday, dst = time.localtime(t)
        return cls(y, m, d)

    @classmethod
    def today(cls):
        t = time.time()
        return cls.fromtimestamp(t)


new_inst = Dates.today()
# ? can I print automatically all of the attributes of an instance?
print(new_inst.y, new_inst.m, new_inst.d)
