# Get student's marks
marks = int(input("Enter your marks: "))

# Determine the grade
if marks >= 85:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: F")