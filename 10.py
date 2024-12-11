data = """my input""".split("\n")

data = [[int(i) for i in j] for j in data]

total = 0
dirs = [(0,1),(1,0),(0,-1),(-1,0)]

for y in range(len(data)):
    for x in range(len(data[0])):
        if data[y][x]==0:
            positions = {(x,y):True}
            for target in range(9):
                newpositions = {}
                for i in positions:
                    for j in dirs:
                        if query(i[0]+j[0],i[1]+j[1],data)==target+1:
                            newpositions[(i[0]+j[0],i[1]+j[1])] = True
                positions = newpositions
            total+=len(positions)
print(total)
            
total = 0

for y in range(len(data)):
    for x in range(len(data[0])):
        if data[y][x]==0:
            positions = [(x,y)]
            for target in range(9):
                newpositions = []
                for i in positions:
                    for j in dirs:
                        if query(i[0]+j[0],i[1]+j[1],data)==target+1:
                            newpositions.append((i[0]+j[0],i[1]+j[1]))
                positions = newpositions
            total+=len(positions)
print(total)
