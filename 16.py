import copy
import heapq
from collections import defaultdict
dirs = {"^":(0,-1),"v":(0,1),">":(1,0),"<":(-1,0)}
def query(x,y,data):
    if not (0<=x<len(data[0]) and 0<=y<len(data)):
        return " "
    else:
        return data[y][x]

data = """my input""".split("\n")

data = [list(i) for i in data]

flag = True

while flag:
    flag = False
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x]!=".":
                continue
            count = 0
            for i in dirs:
                nx = x+dirs[i][0]
                ny = y+dirs[i][1]
                if data[ny][nx] == "#":
                    count+=1
            if count>=3:
                data[y][x] = "#"
                flag = True

keypoints = {}
corners = {}

for y in range(len(data)):
    for x in range(len(data[0])):
        if data[y][x]=="#":
            continue
        options = []
        for i in dirs:
            nx = x+dirs[i][0]
            ny = y+dirs[i][1]
            if data[ny][nx]!="#":
                options.append(i)
        if len(options) >= 3 or data[y][x]!=".":
            keypoints[(x,y)] = options
            if data[y][x] == "S":
                start = (x,y)
            elif data[y][x] == "E":
                end = (x,y)
        elif len(options) == 2:
            if options == ["^","v"] or options == [">","<"]:
                continue
            corners[(x,y)] = options

routes = defaultdict(list)
reverse = {"^":"v","v":"^",">":"<","<":">"}
for i in keypoints:
    for j in dirs:
        for k in dirs:
            if j==k:
                continue
            if reverse[j] == k:
                continue
            if k not in keypoints[i]:
                continue
            routes[(i,j)].append((1000,i,k))

for i in keypoints:
    for j in keypoints[i]:
        x,y = i
        direction = j
        score = 0
        while (x,y) == i or (x,y) not in keypoints:
            x+=dirs[direction][0]
            y+=dirs[direction][1]
            score+=1
            if (x,y) in corners:
                score+=1000
                if reverse[direction] == corners[(x,y)][0]:
                    direction = corners[(x,y)][1]
                else:
                    direction = corners[(x,y)][0]
        routes[(i,j)].append((score,(x,y),direction))

positions = [(0,start,">",False)]
heapq.heapify(positions)
done = {}
best = len(data)*len(data)*1000
howto = defaultdict(dict)

while len(positions)>0:
    score,location,direction,prev = heapq.heappop(positions)
    if (location,direction) in done:
        if done[(location,direction)]==score:
            howto[(location,direction)][prev] = True
        continue
    else:
        howto[(location,direction)][prev] = True
    if score>best:
        break
    if location == end:
        best = score
    done[(location,direction)] = score
    for i in routes[(location,direction)]:
        heapq.heappush(positions,(i[0]+score,i[1],i[2],(location,direction)))

print(best)

positions = []
for i in dirs:
    if(end,i) in howto:
        positions.append((end,i))

visited = defaultdict(list)
total = 0

while len(positions)>0:
    current = positions.pop(0)
    if not current:
        continue
    if current[1] in visited[current[0]]:
        continue
    visited[current[0]].append(current[1])
    for i in howto[current]:
        positions.append(i)
        for j in routes[i]:
            if (j[1],j[2])==current:
                if j[0]==1000:
                    continue
                total+=j[0]%1000-1

total+=len(visited)
print(total)

"""
for i in data:
    print("".join(i))
"""
