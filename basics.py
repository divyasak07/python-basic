print("Hello, World!")


name = "Tejas"
age = 20
marks = 85.5
is_student = True

print(name)
print(age)
print(marks)
print(is_student)



a = 10
b = 5

print(a + b)
print(a * b)
print(a > b)

marks = 75

if marks >= 80:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Grade C")



 for i in range(1, 6):
    print(i)



    i = 1

while i <= 5:
    print(i)
    i += 1



    fruits = ["Apple", "Mango", "Banana"]

print(fruits)
print(fruits[0])
print(fruits[1])


numbers = [10, 20, 30]

numbers.append(40)

print(numbers)







a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

sum = a + b

print("Sum =", sum)


number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")


    a = 10
b = 20

if a > b:
    print("A is largest")
else:
    print("B is largest")


    number = int(input("Enter a number: "))

for i in range(1, 11):
    print(number, "x", i, "=", number * i)



    text = input("Enter a word: ")

reverse = text[::-1]

print("Reverse =", reverse)


number = int(input("Enter a number: "))

if number <= 1:
    print("Not Prime")
else:
    for i in range(2, number):
        if number % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime Number")






        //calculator


        a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    print(a + b)

elif operator == "-":
    print(a - b)

elif operator == "*":
    print(a * b)

elif operator == "/":
    if b != 0:
        print(a / b)
    else:
        print("Cannot divide by zero")

else:
    print("Invalid operator")