def OddOccurring(arr):
    result = 0
    for element in arr:
        result = result^element
    return result

arr = []
n = int(input("Enter array size: "))
while(n):
    num = int(input("Enter the number: "))
    arr.append(num)
    n -=1

print("Occurring number is: ",OddOccurring(arr))