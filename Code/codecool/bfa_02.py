import random


class tresholds:

    def max(self, values):
        maximum = values[0]

        for i in values:
            if i > maximum:
                maximum = i

        return maximum

    def min(self, values):
        minimum = values[0]

        for i in values:
            if i < minimum:
                minimum = i

        return minimum


def fill_funct():
    values = []

    for i in range(10):
        a = random.randint(0, 100)
        values.append(a)

    return values


def main():

    generated_values = fill_funct()

    print(generated_values)

    inst = tresholds()

    print(inst.max(generated_values))
    print(inst.min(generated_values))
    inst.min(generated_values)

main()
