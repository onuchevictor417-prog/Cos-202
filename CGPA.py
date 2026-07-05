# PERSONAL POCKET CGPA CALCULATOR
# ====================================

print("================")
print("     PERSONAL POCKET CGPA CALCULATOR")
print("=================")

courses = int(input("Enter Number of Courses: "))

total_grade_points = 0
total_credit_units = 0

for i in range(1, courses + 1):

    print("\nCourse", i)

    course = input("Course Code: ")

    credit = int(input("Credit Unit: "))

    score = float(input("Score: "))

    # Grade determination using selection statements

    if score >= 70:
        grade = "A"
        point = 5

    elif score >= 60:
        grade = "B"
        point = 4

    elif score >= 50:
        grade = "C"
        point = 3

    elif score >= 45:
        grade = "D"
        point = 2

    elif score >= 40:
        grade = "E"
        point = 1

    else:
        grade = "F"
        point = 0

    print("Grade:", grade)
    print("Grade Point:", point)

    total_grade_points += point * credit
    total_credit_units += credit

cgpa = total_grade_points / total_credit_units

print("\n==========================")
print("TOTAL CREDIT UNITS =", total_credit_units)
print("TOTAL GRADE POINTS =", total_grade_points)
print("CGPA =", round(cgpa, 2))
print("==========================")

# CGPA Classification

if cgpa >= 4.50:
    print("Class of Degree: First Class")

elif cgpa >= 3.50:
    print("Class of Degree: Second Class Upper")

elif cgpa >= 2.40:
    print("Class of Degree: Second Class Lower")

elif cgpa >= 1.50:
    print("Class of Degree: Third Class")

elif cgpa >= 1.00:
    print("Class of Degree: Pass")

else:
    print("Class of Degree: Fail")
