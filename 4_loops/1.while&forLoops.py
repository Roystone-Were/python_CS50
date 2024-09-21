# animal = "Cat"

# for _ in range(1,6):
#     print(animal)

# i = 0
# while i < 3:
#     print("cat")
#     i += 1

# print("cat\n" *3, end="")

# while True:
#     num = int(input("Enter A number: "))
#     if num > 0:
#         break
# for _ in range(num):
#     print("CAT")

def main():
    num = get_number()
    output(num)
    

def get_number():
    while True:
        num = int(input("Enter Age: "))
        if num > 0:
            break
    return num

def output(num):
    for _ in range(num):
        print(f"Your Age Is {num}")
        
    
main()
