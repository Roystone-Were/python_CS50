# Main function that handles user input for name, age, and number checking
def main():
    name = input("what is your Name\n").capitalize().strip()
    age = int(input("what is your Age\n"))
    check_age(name, age)
    number_checker()
    
#checks the age if its either a minor, adult or senior
def check_age(name, age):
    if age < 18:
        print(f"{name}, you are  {age} years old and you are a minor")
    elif age >= 18 and age <65:
        print(f"{name}, you are {age} years old and you are an Adult")
    else:
        print(f"{name}, you are {age} years old and you are  a Senior")
        
# Function to check if a number is even or odd, and also check for FizzBuzz conditions
def number_checker():
    num = int(input(("Enter a number\n")))
    if num%2 == 0:
        print(f"{num} is an even number")
    else:
        print(f"{num} is an odd number")
        
#Chek if number  is divisible by 3, five or both
    if num % 3 == 0 and num % 5 == 0:
        print(f"{num}- FizzBuzz")
    elif num % 5 == 0:
        print(f"{num}- Buzz")
    elif num % 3  == 0:
        print(f"{num}- Fizz")
    else:
        print(f"{num}, None")
main()
    
    