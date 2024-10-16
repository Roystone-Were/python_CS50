import csv  # Import the csv module to work with CSV files

# Prompt the user for their name and store it in the 'name' variable
name = input("What's your name? ")

# Prompt the user for their favorite pet and store it in the 'pet' variable
pet = input("What's your favorite pet? ")

# Open the 'students.csv' file in append mode
# 'a' means new data will be added to the end of the file
# 'newline=""' ensures no extra blank lines are added between rows in the CSV
