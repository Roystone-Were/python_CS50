def square_number():
    num = int(input("enter a number\n"))
    print(display_square(num))
    
def display_square(num):
    return(f"the Square of {num} is {num **2}")

square_number()
