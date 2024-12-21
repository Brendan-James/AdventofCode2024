data = """my input""".split("\n")

for y in range(len(data)):
    for x in range(len(data[0])):
        if data[y][x] == "S":
            start = (x,y)
        if data[y][x] == "E":
            end = (x,y)

path = [0,start]
while path[-1] != end:
    x,y = path[-1]
    for i in dirs:
        nX = x+dirs[i][0]
        nY = y+dirs[i][1]
        if (nX,nY) == path[-2]:
            continue
        if data[nY][nX] != "#":
            path.append((nX,nY))
            break
path = path[1:]

steps = {}
for i,v in enumerate(path):
    steps[v] = i

count = 0
for y in range(len(data)):
    for x in range(len(data[0])):
        if data[y][x] != "#":
            continue
        options = []
        for i in dirs:
            nX = x+dirs[i][0]
            nY = y+dirs[i][1]
            if (nX,nY) in steps:
                options.append(steps[(nX,nY)])
        if len(options)==2:
            cheat = abs(options[0]-options[1])-2
            if cheat>=100:
                count+=1
print(count)
count = 0
for A,i in enumerate(path):
    for B,j in enumerate(path):
        if A-B<=100:
            continue
        manhat = abs(i[0]-j[0])+abs(i[1]-j[1])
        if manhat<=20:
            if A-B>=100+manhat:
                count+=1
print(count)
