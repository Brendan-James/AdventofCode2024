data = """my input""".split("\n")

data = [i.split("   ") for i in data]

dataA = sorted([int(i[0]) for i in data])
dataB = sorted([int(i[1]) for i in data])

total1 = 0

for i in range(len(dataA)):
    total1+=abs(dataA[i]-dataB[i])
print(total1)

total2 = 0
for i in dataA:
    for j in dataB:
        if i==j:
            total2+=i
print(total2)
