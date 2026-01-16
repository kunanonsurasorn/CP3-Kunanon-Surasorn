def addition_number(a,b):
    print(f"{a} + {b} = {a+b}")

def subtraction_number(a,b):
    print(f"{a} - {b} = {a-b}")

def multiplication_number(a,b):
    print(f"{a} * {b} = {a*b}")

def division_number(a,b):
    print(f"{a} / {b} = {round(a/b,2)}")

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
addition_number(a,b)
subtraction_number(a,b)
multiplication_number(a,b)
division_number(a,b)
