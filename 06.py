import copy
data = """my input""".split("\n")

for x in range(len(data[0])):
    for y in range(len(data)):
        if data[y][x]=="^":
            guard = (x,y,0)
goppy = copy.deepcopy(guard)
def query(x,y,data):
    if not (0<=x<len(data[0]) and 0<=y<len(data)):
        return "."
    else:
        return data[y][x]

positions = {}
dirs = [(0,-1),(1,0),(0,1),(-1,0)]
while 0<=guard[0]<len(data[0]) and 0<=guard[1]<len(data):
    positions[(guard[0],guard[1])] = True
    target = (guard[0]+dirs[guard[2]][0],guard[1]+dirs[guard[2]][1])
    if query(target[0],target[1],data)!="#":
        guard = (target[0],target[1],guard[2])
    else:
        guard = (guard[0],guard[1],(guard[2]+1)%4)

print(len(positions))


# pt 2 is slow but that's life I guess
count = 0
copied = [list(i) for i in data]
for x in range(len(data[0])):
    for y in range(len(data)):
        if (x,y) not in positions:
            continue
        print(x,y)
        guard = copy.deepcopy(goppy)
        if x == guard[0] and y==guard[1]:
            continue
        data = copy.deepcopy(copied)
        data[y][x]="#"
        positions2 = {}
        dirs = [(0,-1),(1,0),(0,1),(-1,0)]
        while 0<=guard[0]<len(data[0]) and 0<=guard[1]<len(data):
            if (guard[0],guard[1],guard[2]) in positions2:
                count+=1
                break
            positions2[(guard[0],guard[1],guard[2])] = True
            target = (guard[0]+dirs[guard[2]][0],guard[1]+dirs[guard[2]][1])
            if query(target[0],target[1],data)!="#":
                guard = (target[0],target[1],guard[2])
            else:
                guard = (guard[0],guard[1],(guard[2]+1)%4)
print(count)
