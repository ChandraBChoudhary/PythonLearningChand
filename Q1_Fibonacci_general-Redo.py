num1 = 0
num2 = 1
counter = 0

limit = int(input("How many numbers of fibonacci series you require : "))
print("Fibonacci series are : ")
print(num1)
print(num2)
for counter in range(limit - 2):
    num1 = num1 +num2 
    print(num1)
    num1, num2 = num2 ,num1 
    
