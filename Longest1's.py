num = int(input("Enter the number: "))
a = bin(num)[2:]
print("The binary of", num, "=", a)
print("Longest consecutive 1's in the binary value of", num, "is:-")

def ones(x):
    count = 0
    while x != 0:
        x = x & (x >> 1)
        count += 1
    return count

print(ones(num))
