# THIS IS A LIST OF DICTIONARIES
# This script iterates through a list of dictionaries where each dictionary contains
# student information: 'name', 'location', and 'Status'. It prints the student's
# name, location, and status separated by commas.
students =[
    {"name": "Roy", "location":"Donholm", "Status": "Rich"},
    {"name": "Young", "location":"Donholm", "Status": "Rich"},
    {"name": "Milton", "location":"Karen", "Status": "Rich"},
    {"name": "Jr", "location":"Kisumu", "Status": "Rich"},
]

for student in students:
    print(student["name"], student["location"], student["Status"], sep= ", ")