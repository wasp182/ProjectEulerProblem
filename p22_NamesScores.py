with open("0022_names.txt","r") as f1:
    data = f1.readline().replace("\"","").split(",")

# data = ["COLIN","COLIN"]
# print(data)
data.sort()
print(data)
sums = 0
for index , items in enumerate(data):
    word_sums = 0
    for k in items:
# A is 65 , index is back to 1 by subtracting 64
        word_sums += (ord(k)-64)
    sums += word_sums*(index+1)

print(sums)