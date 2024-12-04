data = """my input""".split("\n")

dirs = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]

def query(x,y,data):
    if not (0<=x<len(data[0]) and 0<=y<len(data)):
        return "."
    else:
        return data[y][x]
total = 0
xmas = "XMAS"
for x in range(len(data[0])):
    for y in range(len(data)):
        for d in dirs:
            for n in range(4):
                if query(x+d[0]*n,y+d[1]*n,data)!=xmas[n]:
                    break
            else:
                total+=1
print(total)
total2 = 0

dirs2 = [((1,1),(-1,1)),((1,1),(1,-1)),((-1,-1),(1,-1)),((-1,-1),(-1,1))]
for x in range(len(data[0])):
    for y in range(len(data)):
        if data[y][x] == "A":
            for d in dirs2:
                if query(x+d[0][0],y+d[0][1],data) == "M" and query(x+d[1][0],y+d[1][1],data) == "M" and query(x-d[0][0],y-d[0][1],data) == "S" and query(x-d[1][0],y-d[1][1],data) == "S":
                    total2+=1

print(total2)
