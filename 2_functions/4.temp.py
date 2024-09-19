
#convert from fahrenheit to celcius
def to_celsius(): 
    fahrenheit = int(input("Enter Temperature in fahrenheit\n"))
    return print((fahrenheit - 32)* (5/9)) 

#convert from celcius to fheigt
def to_fheit():
    celsius = int(input("Enter Temp in celsius\n"))
    return print((celsius * 9/5 ) + 32)

def main():
    choice = input("Type 'F' to convert from Fahrenheit to celsius, or 'C' to Convert from Celsius to Farenheit\n")
    
    if choice == 'F' or 'f':
        to_celsius()
    elif choice == 'C' or 'c':
        to_fheit()
    else:
        print("Invalid Choice, Enter 'F' or 'C'" )
main()