import csv

name = input("Whats your name? ")
pet = input("Whats your favorite Pet? ")

with open("students.csv", "a", newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["name", "pet"])
    writer.writerow({"name": name, "pet": pet})