#swapping 2 numbers
num1 = int(input("Enter num1: "))
num2 = int (input("Enter num2: "))

#Method 1
def swap1(a, b):
    a = a^b
    b = a^b
    a = a^b
    print("After swapping: num1 = ",a," num2 = ",b)

#Method 2
def swap2(a, b):
    a = (a&b)+(a|b)
    b = a+(~b)+1
    a = a+(~b)+1
    print("After swapping: num1 = ",a," num2 = ",b)

#Method 3
def swap3(a, b):
    a = a+b
    b = a-b
    a = a-b
    print("After swapping: num1 = ",a," num2 = ",b)

swap1(num1, num2)
swap2(num1, num2)
swap3(num1, num2)