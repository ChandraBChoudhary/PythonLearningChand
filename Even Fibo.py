''' First 10 even fibonacci series'''

num=0
num1=1
print("First 10 even Fibonacii series are : ")
print(num)
counter=0
for x in range(30) :
    fibo=num+num1
    if (fibo%2==0):
        print(fibo)
    num=num1
    num1=fibo
