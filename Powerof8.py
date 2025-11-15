n = int(input("Enter the number: "))

if n > 0 and (n % 8 == 0 and (n & (n - 1)) == 0):
    print("Number is a PowerOf8")
else:
    print("Number is not a PowerOf8")
