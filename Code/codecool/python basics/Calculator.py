print("Please write the first number")
number1 = int(input())

print("Now choose one operator")
operator = input()

print("Please write the second number")
number2 = int(input())

if operator == "+" :
   print(number1 + number2)

if operator == "-": 
   print(number1 - number2)

if operator == "*":
   print(number1 * number2)

if operator == "/":
   print(number1 / number2)