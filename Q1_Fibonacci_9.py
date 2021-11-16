# First 9 fibonacci series
num=0
num1=1
print("Fibonacii series are : ")
print(num)
print(num1)
for x in range(7) :
    fibo=num+num1
    print(fibo)
    num=num1
    num1=fibo
