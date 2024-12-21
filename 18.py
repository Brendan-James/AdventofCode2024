import heapq
dirs = {"^":(0,-1),"v":(0,1),">":(1,0),"<":(-1,0)}
def query(x,y,data):
    if not (0<=x<len(data[0]) and 0<=y<len(data)):
        return " "
    else:
        return data[y][x]

data = """my data""".split("\n")

data = [[int(j) for j in i.split(",")] for i in data]

size = 70
zone = [["." for i in range(size+1)] for j in range(71)]

for i in range(1024):
    x,y = data[i]
    zone[y][x] = "#"

positions = [(0,(0,0))]
heapq.heapify(positions)
visited = {}

while len(positions)>0:
    score, location = heapq.heappop(positions)
    if location in visited:
        continue
    if location == (size,size):
        print(score)
        break
    visited[location] = score
    x,y = location
    for i in dirs:
        newX = x+dirs[i][0]
        newY = y+dirs[i][1]
        if query(newX,newY,zone)==".":
            heapq.heappush(positions,(score+1,(newX,newY)))

for i,v in enumerate(data):
    if i<1024:
        continue
    current = v
    zone[v[1]][v[0]] = "#"
    positions = [(0,(0,0))]
    heapq.heapify(positions)
    visited = {}

    while len(positions)>0:
        score, location = heapq.heappop(positions)
        if location in visited:
            continue
        if location == (size,size):
            break
        visited[location] = score
        x,y = location
        for i in dirs:
            newX = x+dirs[i][0]
            newY = y+dirs[i][1]
            if query(newX,newY,zone)==".":
                heapq.heappush(positions,(score+1,(newX,newY)))
    else:
        print(",".join([str(x) for x in current]))
        break
