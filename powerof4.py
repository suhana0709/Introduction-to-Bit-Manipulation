num=int(input("Enter the number: "))
if num > 0 and (num & (num-1) == 0 and (num%3==1)):
    print("Number is a PowerOf4")
else:
    print("Number is not a PowerOf4.")