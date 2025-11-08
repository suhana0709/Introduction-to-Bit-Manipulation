#finding the number of set and non set bits


def numberofbits(n):
    zero = 0
    one = 0
    while(n):
        if (n & 1 == 1):
            one += 1
        else:
            zero += 1
        n >>= 1
    print("Number of one: ",one)
    print("Number of zeros: ",zero)

number = int(input("Enter your number: "))

numberofbits(number)