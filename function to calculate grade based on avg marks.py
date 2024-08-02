# Function to calculate the grade based on average marks
def calculate_grade(average):
    if 90 <= average <= 100:
        return 'A'
    elif 80 <= average < 90:
        return 'B'
    elif 70 <= average < 80:
        return 'C'
    elif 60 <= average < 70:
        return 'D'
    else:
        return 'F'

# Get marks for 5 subjects from the user
marks_subject1 = float(input("Enter marks for subject 1: "))
marks_subject2 = float(input("Enter marks for subject 2: "))
marks_subject3 = float(input("Enter marks for subject 3: "))
marks_subject4 = float(input("Enter marks for subject 4: "))
marks_subject5 = float(input("Enter marks for subject 5: "))

# Calculate total and average
total_marks = marks_subject1 + marks_subject2 + marks_subject3 + marks_subject4 + marks_subject5
average_marks = total_marks / 5

# Calculate grade
grade = calculate_grade(average_marks)

# Display the results
print("\nTotal Marks: {:.2f}".format(total_marks))
print("Average Marks: {:.2f}".format(average_marks))
print("Grade: {}".format(grade))
