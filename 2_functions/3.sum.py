def sum():
    num1 = int(input("Enter First Number\n"))
    num2 = int(input("Enter Second Number\n"))
    (display_sum(num1, num2))

def display_sum(num1, num2):
    return print(f"Sum of {num1} and {num2} is {num1 + num2}")

sum()