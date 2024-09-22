#SIMPLE DICTIONARY
students = {
    "Roy": "Donholm", 
    "Prince":"Donholm", 
    "Junior":"Fedha"
    }

#.items() method returns keys(student names) and values (location) in the dictionaries
for student in students:
    print(student, students[student], sep=", ")