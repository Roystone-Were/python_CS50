import csv  # Importing the csv module to handle reading/writing CSV files

students = []  # Initialize an empty list to store student data

# Open the 'student.csv' file in read mode
with open("student.csv", "r") as file:
    # Use DictReader to read the CSV file into dictionaries, where each row is a dictionary
    reader = csv.DictReader(file)
    
    # Iterate over each row in the CSV file
    for row in reader:
        students.append(row)  # Append each row (as a dictionary) to the 'students' list

# Sort the list of students by the 'name' field using a lambda function as the key
for student in sorted(students, key=lambda student: student["name"]):
    # Print the student's name and the pet they love, formatted as "Name loves Pet"
    print(f"{student['name']} loves {student['pet']}")
    #the 'student.csv' file has the 'name,pet' as headers to enable read
