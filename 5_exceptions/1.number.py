def main():
    x = get_int()  # Call the get_int function to get a valid integer from the user
    print(f"The number is {x}")  # Print the valid integer entered by the user

def get_int():
    while True:  # Start an infinite loop that continues until a valid integer is returned
        try:
            return int(input("Enter a Number: "))  # Prompt user to enter a number and attempt to convert it to an integer
        except ValueError:
            print("Enter a Valid Value!")  # Inform the user when they enter an invalid input
            
main()  # Call the main function to start the program
