def find_factorial():
    n = check_positive()
    result = factorial(n)
    print(f"The fuctorial of {n} is {result}")


def check_positive():
    while True:
        try:
            n = int(input("Enter a positive number: "))
            if n > 0:
                return n
            else:
                print("Enter A positive Number")
        
        except ValueError:
            print("Enter a Valid number")
            
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n -1)
            
find_factorial()