def power2(num):
    if num<=0:
        return False
    elif num & (num-1)==0:
        print("YES!", num," is a power of 2.")
    else:
        print("NO!", num," is not a power of 2.")

num = int(input("Enter the number: "))
power2(num)