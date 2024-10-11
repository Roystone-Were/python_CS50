import sys  # Import the sys module to access command-line arguments

# Check if the number of command-line arguments is less than 2
if len(sys.argv) < 2:
    # Exit the program and print an error message if there are not enough arguments
    sys.exit("Few Arguments")

# Iterate over each command-line argument starting from the second one
for arg in sys.argv[1:]:
    # Print a message that includes the current argument
    print("my name is", arg)

