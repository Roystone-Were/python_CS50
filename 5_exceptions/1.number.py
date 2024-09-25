def main():
    x = get_int()
    print(f"The number is {x}")  # Print the valid integer entered by the user


def get_int():
    while True:  # Start an infinite loop that continues until a break statement is encountered
        try:
            x = int(input("Enter a Number: "))  # Prompt user to enter a number and try to convert it to an integer
        except ValueError:
            print("x is not an integer")  # If the conversion fails, print an error message
        else: 
            break  # Exit the loop if the input is successfully converted to an integer
    return x
main()

