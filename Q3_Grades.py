max = 100

print("Please enter the marks for following subjects to know the result")
Eng =  int(input("English : "))
Maths =  int(input("Mathematics : "))
Science =  int(input("Science : "))

percentage = (Eng + Maths + Science) * max / 300

if(percentage >= 90 and percentage <= 100) :
    grade = "Grade A"
elif percentage >= 80 and percentage < 90 :
    grade = "Grade B"
elif percentage < 35 :
    grade = "Fail"
else :
    grade = "Average"
print("Your result is :", grade)
