def SetorNot(number, n):
    #u need to define 'mask before using it
    mask = 1   #assuming u want to check if the bit is set or not
    if (n & mask) == 1   or  (n & mask) == 0:       #corrected comparision and OR operator
        if number & (1 << (n-1)):
            print("SET")
        else:
            print("NOT SET")

number = int(input("Enter the number: "))
n = int(input("Enter the bit position: "))

SetorNot(number, n)