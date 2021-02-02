with open("./file1.txt") as file:
    file1 = [n.strip("\n") for n in file.readlines()]

with open("./file2.txt") as file:
    file2 = [n.strip("\n") for n in file.readlines()]

common_numbers = [int(n) for n in file1 if n in file2]

print(common_numbers)