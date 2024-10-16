import csv 

name = input("What's your name? ") 
pet = input("What's your favorite pet? ")

# Open the 'students.csv' file in append mode (so data is added at the end of the file)
# The 'newline=""' ensures no extra blank lines are written between rows
with open("students.csv", "a", newline='') as file:
     # Create a DictWriter object, specifying the fieldnames (i.e., columns 'name' and 'pet')
     writer = csv.DictWriter(file, fieldnames=["name", "pet"])
     
     # Write a row with the collected name and pet data
     writer.writerow({"name": name, "pet": pet})