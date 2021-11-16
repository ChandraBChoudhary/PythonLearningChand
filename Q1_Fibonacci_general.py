# generating fibonacci series for the limit provided by user
num=0
num1=1
limit = int(input(" Please enter a number to generate fibonacci series : "))
print("Fibonacii series are : ")
print(num)
print(num1)

for x in range(limit-2) :
    fibo=num+num1
    print(fibo)
    num=num1
    num1=fibo

# Can be improved as below
# generating fibonacci series for the limit provided by user
num=0
num1=1
limit = int(input(" Please enter a number to generate fibonacci series : "))
if limit <=1 :
    print("please enter a number greater than 1")
else:
    print("Fibonacii series are : ")
    print(num)
    print(num1)
    
for x in range(limit-2) :
    fibo=num+num1
    print(fibo)
    num=num1
    num1=fibo
