import csv

data = []
with open("p13.txt",'r') as inputsteam:
    for lines in inputsteam:
        lines = lines.strip("\n")
        data.append(int(lines[:12]))

# with open("p13.txt",'r') as inputsteam:
#     data = csv.reader(inputsteam,delimiter="\n")
#     for lines in data:
#         print(lines)

print(data)
sum = 0
for items in data:
    sum += items
print(sum)

