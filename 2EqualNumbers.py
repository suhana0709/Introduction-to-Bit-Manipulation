def CheckIfSame(num1, num2):
    if ((num1 ^ num2) != 0):
        print("Both numbers are not equal.")
    else:
        print("Both numbers are equal.")

print("Checking if two numbers are equal or not:-\n")
num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))
CheckIfSame(num1, num2)