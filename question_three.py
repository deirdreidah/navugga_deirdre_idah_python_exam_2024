#3(i)
age = int(input("Enter age: "))
if age >= 18:
    print("You are eligible")
else:
    print("You are not eligible")

#3(ii)
def grade_students(marks):
    if 90 <= marks <= 100:
        return 'A'
    elif 80 <= marks < 90:
        return 'B'
    elif 70 <= marks < 80:
        return 'C'
    elif 60 <= marks < 70:
        return 'D'
    else:
        return 'F'
print(grade_students(85)) 

#3(iv)
def grade_students(marks):
    if 90 <= marks <= 100:
        return 'A'
    elif 80 <= marks < 90:
        return 'B'
    elif 70 <= marks < 80:
        return 'C'
    elif 60 <= marks < 70:
        return 'D'
    elif 0 <= marks < 60:
        return 'F'
    else:
        return 'Invalid Input'
print(grade_students(60)) 

#3(v)
def grade_students(marks):
        if 90 <= marks <= 100:
            return 'A', 'Excellent'
        elif 80 <= marks < 90:
            return 'B', 'Excellent'
        elif 70 <= marks < 80:
            return 'C', 'Good'
        elif 60 <= marks < 70:
            return 'D', 'Satisfactory'
        else:
            return 'F', 'Needs Improvement'
marks, comment = grade_students(78)
print(f"Grade: {marks} Comment: {comment}") 


               