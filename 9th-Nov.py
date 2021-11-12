'''
Find the time taken by sandeep to travel 10000 km '''

Total_Distance = 10000
Avg_Speed = 1

Time = Total_Distance // Avg_Speed
Avg_hours = 3 

Days = Time // Avg_hours
Rem_hrs = Time % Avg_hours

Months = Days // 30
Rem_days = Days % 30

Year = Months // 12
Rem_months = Months % 12

print(Year," years",Rem_months,"Months", Rem_days,"days", Rem_hrs,"hr")

'''find the count of elements in list'''

string = "Bangaluru is the capital of Karnataka"
stack = string.split()
count = 0
for test in stack :
    count += 1
    print("list contains", test)
    
print("count = " , count)
for num in range(95,102):
    # print(num/2)
    if(num<=99):
        print(num/2)    
    elif(num>99):
        print(num*2)
    else:
        print("NUM")
        
        
        
counter = 0
while counter < 6:
    print("Hello World")
    counter +=1


