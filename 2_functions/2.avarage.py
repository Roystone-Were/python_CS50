def inputs():
    num1 = int(input("Enter first Number"))
    num2 = int(input("Enter Second Number"))
    num3 = int(input("Enter Third Number"))
    avarage(num1,num2,num3)

def avarage(num1, num2, num3):
    return print(f"The avarage of {num1}, {num2}, {num3} is {(num1 + num2 + num3)/3}")

inputs()