print("#Find the power!!!\n")
x = int(input("Enter the base value(x) for x**y (x to the power y): "))
y = int(input("Enter the power value(y) for x**y (x to the power y): "))

for i in range (y):
    result = 1
    result = x*x

print(x," to the power ",y,": ",result)