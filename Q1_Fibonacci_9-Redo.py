num1 = 0
num2 = 1
counter = 0
print("Frst 9 fibonacci series are : ")
print(num1)
print(num2)
for counter in range(7):
    num1 = num1 +num2 
    print(num1)
    num1,num2 = num2 , num1 
