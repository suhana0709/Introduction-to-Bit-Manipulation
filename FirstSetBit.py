def firstsetbit(n):
    if (n & 1) == 1:
        print("The rightmost bit is a SET.")

n = int(input("Enter a number: "))
firstsetbit(n)