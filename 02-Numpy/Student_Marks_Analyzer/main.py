# project 1 : Student Marks Analyzer Using Numpy 

import numpy as np
students = np.array(["John","Aakash","Ramesh","Chaitanya","Vikram"])
marks = np.array([
    [85, 90, 78],
    [92, 88, 95],
    [70, 65, 72],
    [88, 91, 84],
    [55, 60, 58]
])

# printing the student names and their marks
for i in range(len(students)):
    print(f"Student: {students[i]}, Marks: {marks[i]}")

#  calculating the average marks for each student
average_marks = np.mean(marks, axis=1)
for i in range(len(students)):
    print(f"Average marks of {students[i]}: {average_marks[i]}")
    
    
# create marksheet of students 
 
print("="*50)
print("    STUDENT MARKSHEET")
print("="*50)


# display all students
print("\nstudent list :")
for i in range(len(students)):
    print(f"{i+1}.{students[i]}")
    
# ask user to select a student
choice = int(input("enter the student number (1-5)"))

# convert choice to index
index = choice - 1

# get the selected student's marks 
student_marks = marks[index]

# calculate total and average marks
total_marks = np.sum(student_marks)
average_marks = np.mean(student_marks)

# calculate percentage
percentage = (total_marks / 300)*100

# find highest and lowest marks
highest_marks = np.max(student_marks)
lowest_marks = np.min(student_marks)

# grade calculation
if percentage >= 90:
    grade = "A+"
elif  percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >=60:
    grade="C"
elif percentage >=50:
    grade = "D"
else:
    grade = "F"

# pass/fail status

if percentage >= 40:
    status = "pass"
else:
    status = "fail"

# Display the Marksheet
print("\n")
print("="*50)
print("       STUDENT MARKSHEET")
print("="*50)

print(f"Student Name: {students[index]}")

print("-" * 50)
print(f"{'Subject':<20}{'Marks'}")
print("-" * 50)

subjects = ["Math", "Science", "English"]

for i in range(len(subjects)):
    print(f"{subjects[i]:<20}{student_marks[i]}")
    
print("-" * 50)

print(f"Total Marks        : {total_marks}")
print(f"Average Marks      : {average_marks:.2f}")
print(f"Percentage         : {percentage:.2f}%")
print(f"Highest Marks      : {highest_marks}")
print(f"Lowest Marks       : {lowest_marks}")
print(f"Grade              : {grade}")
print(f"Result             : {status}")

print("=" * 50)