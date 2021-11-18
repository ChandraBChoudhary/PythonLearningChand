result = {}
marks = [ 78, 89, 85, 91, 93, 82, 79 ]
roll_number = [1,2,3,4,5,6,7]
for key in roll_number:
    for value in marks:
        result[key] = value
        marks.remove(value)
        break  
    
print("The result of all students is : ", result)
highest_score = max(result, key=result.get)
print("The role number of student who scored highest marks is :", highest_score)
