def query(x,y,data):
    if not (0<=x<len(data[0]) and 0<=y<len(data)):
        return " "
    else:
        return data[y][x]

data = """my input""".split("\n")

visited = {}

dirs = [(0,1),(1,0),(0,-1),(-1,0)]
total = 0

for x in range(len(data[0])):
    for y in range(len(data)):
        if (x,y) not in visited:
            target = data[y][x]
            todo = [(x,y)]
            perim = 0
            area = 0
            while len(todo)>0:
                current = todo.pop()
                if query(current[0],current[1],data)!=target:
                    perim += 1
                    continue
                if current in visited:
                    continue
                visited[current] = True
                area+=1
                for i in dirs:
                    todo.append((current[0]+i[0],current[1]+i[1]))
            total+=perim*area

print(total)

visited = {}
total = 0

for y in range(len(data)):
    for x in range(len(data[0])):
        if (x,y) not in visited:
            target = data[y][x]
            todo = [(x,y,...)]
            area = 0
            count = 0
            perim = {}
            while len(todo)>0:
                current = todo.pop()
                fromdir = current[2]
                current = current[:2]
                if query(current[0],current[1],data)!=target:
                    perim[(current,fromdir)] = True
                    count+=1
                    continue
                if current in visited:
                    continue
                visited[current] = True
                area+=1
                for i in dirs:
                    todo.append((current[0]+i[0],current[1]+i[1],i))
            for i,fromdir in perim:
                for x,j in enumerate(dirs[:2]):
                    if ((i[0]+j[0],i[1]+j[1]),fromdir) in perim:
                        count-=1
            total+=count*area
            #print(target,area,count,count*area)

print(total)
