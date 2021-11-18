marks = [ 78, 89, 85, 91, 93, 82, 79 ]
total = 0 
denominator = len(marks)
for ele in range(0, denominator):
    total = total + marks[ele]
    Average_marks = total / denominator
    
print("Average marks scored by student is: " , Average_marks)
