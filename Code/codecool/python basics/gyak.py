def underline(title):
    return title + '\n' + ('+' * len(title))

print (underline("apple"))


def underline2(title2):
    length = len(title2)
    return title2 + ("\n" + "+" * length)

print (underline("apple"))

apple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
apple_enum = enumerate(apple)
print(apple_enum)

#[[row[i] for row in matrix] for i in range(4)]
#[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
betuk = ["A", "B", "C"]
my_matrix = [[y for y in betuk] for x in range(4)]
print(my_matrix)


def list_compr(begin_number, end_number):
    my_list = [x for x in range(begin_number, end_number + 1)]
    return my_list

# print(list_compr(2, 10))


def percent(value, total):
    return"%3d" % ((value) / total * 100)

print(percent(46, 90))
print(percent(63, 12))


def getSumOfLastDigits(numList):
    for i in range(len(numList)):
        numList[i] = str(numList[i])

    summa = 0

    for j in range(len(numList)):
        summa += numList[j[-1]]

numbers1 = [2, 3, 4]
numbers2 = [1, 23, 456]

print(getSumOfLastDigits(numbers1))
print(getSumOfLastDigits(numbers2))
# print(getSumOfLastDigits(numbers3))
