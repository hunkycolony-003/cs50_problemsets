import csv


with open("pseudo2.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name","home"])
    writer.writeheader()

line = "    writer = csv.DictWriter(file, fieldnames=["name","home"]) ".strip()
print(line)
