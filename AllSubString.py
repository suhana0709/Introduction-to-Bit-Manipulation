import math

def PrintPowerSet(set, SetSize):
    PowerSetSize = int(math.pow(2, SetSize))
    for outer in range(PowerSetSize):
        for inner in range(SetSize):
            if (outer & (1 << inner)) > 0:
                print(set[inner], end=" ")
        print()

size = int(input("Enter the array size: "))
set = [str(input("Enter the element: ")) for _ in range (size)]
print(PrintPowerSet(set, len(set)))