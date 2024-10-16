# Open the file 'names.txt' in read mode 
with open("names.txt", "r") as file:
    # Sort the lines from the file while iterating over them
    for line in sorted(file): 
        # Print each line with "Hello", removing any trailing newline characters from the right      
        print("Hello", line.rstrip())