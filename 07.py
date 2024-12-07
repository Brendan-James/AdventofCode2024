data = """my input""".split("\n")

data = [i.split(": ") for i in data]
data = [[int(i[0]),[int(j) for j in i[1].split(" ")]] for i in data]

count = 0
for i in data:
    values = {i[1][0]:True}
    for j in i[1][1:]:
        newvalues = {}
        for k in values:
            newvalues[k+j] = True
            newvalues[k*j] = True
        values = newvalues
    if i[0] in values:
        count+=i[0]

print(count)


count = 0
for i in data:
    values = {i[1][0]:True}
    for j in i[1][1:]:
        newvalues = {}
        for k in values:
            if k>i[0]:
                continue
            newvalues[k+j] = True
            newvalues[k*j] = True
            newvalues[int(str(k)+str(j))] = True
        values = newvalues
    if i[0] in values:
        count+=i[0]

print(count)
