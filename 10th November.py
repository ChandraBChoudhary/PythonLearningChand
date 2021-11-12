'''
Find the time taken by sandeep to travel 10000 km '''


Total_Distance = 10000
Avg_Speed = 1
#################################find the pattern
Time = Total_Distance // Avg_Speed
Avg_hours = 3 
#################################find the pattern
Days = Time // Avg_hours
Rem_hrs = Time % Avg_hours
#################################find the pattern
Months = Days // 30
Rem_days = Days % 30
#################################find the pattern
Year = Months // 12
Rem_months = Months % 12

print(Year," years",Rem_months,"Months", Rem_days,"days", Rem_hrs,"hr")

'''
Find the time taken by sandeep to travel 10000 km '''
def divide(num, den)=:
    quo = num // den
    rem = num % den
    return quo , rem

Total_Distance = 10000
Avg_Speed = 1
Time = Total_Distance // Avg_Speed
Avg_hours = 3 
#################################find the pattern
Days , Rem_hrs = divide(Time, Avg_hours)
#################################find the pattern
Months, Rem_days = divide(Days , 30)
#################################find the pattern
Year, Rem_months = divide(Months, 12)

print(Year," years",Rem_months,"Months", Rem_days,"days", Rem_hrs,"hr")
