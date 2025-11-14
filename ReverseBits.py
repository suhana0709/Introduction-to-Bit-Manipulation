def convert(n):
    r=bin(n)[2:]
    a=r[::-1]
    j=int(a,2)
    return j

n=int(input("Enter the number:"))
print("Reversed integer number: ",convert(n))