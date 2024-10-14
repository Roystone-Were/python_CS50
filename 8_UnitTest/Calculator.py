def main():
    x = input("Enter a number: ")
    print(f"the square for {x} is", square(x))
    
def square(n):
    return n * n

if __name__ == "__main__": #this avoids main being run unexpectedley
    main()
    
#we create the other file <test_calculator.py> to test it