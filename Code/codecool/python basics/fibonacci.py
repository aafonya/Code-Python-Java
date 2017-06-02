fibonacci = [0, 1]

for i in range(0, 28):
    fibonacci.append(fibonacci[i] + fibonacci[i + 1])

print(fibonacci)
