import copy

data = """my input""".split("\n\n")

area = [list(i) for i in data[0].split("\n")]
area2 = copy.deepcopy(area)

moves = []
for i in data[1].split("\n"):
    for j in i:
        moves.append(j)

dirs = {"<":(-1,0),">":(1,0),"^":(0,-1),"v":(0,1)}

components = {}

for y in range(len(area)):
    for x in range(len(area[0])):
        if area[y][x]=="@":
            playerX = x
            playerY = y

def move(x,y,direction,moving,data):
    if data[y+direction[1]][x+direction[0]] == ".":
        data[y+direction[1]][x+direction[0]] = moving
        data[y][x] = "."
        return True
    elif data[y+direction[1]][x+direction[0]] == "#":
        return False
    elif data[y+direction[1]][x+direction[0]] == "O":
        if move(x+direction[0],y+direction[1],direction,"O",data):
            data[y+direction[1]][x+direction[0]] = moving
            data[y][x] = "."
            return True
    return False

for i in moves:
    if move(playerX,playerY,dirs[i],"@",area):
        playerX+=dirs[i][0]
        playerY+=dirs[i][1]

total = 0

for y in range(len(area)):
    for x in range(len(area[0])):
        if area[y][x]=="O":
            total+=y*100+x

for i in area:
    print("".join(i))

print(total)

area = []

widen = {"#":"##","O":"[]","@":"@.",".":".."}

for i in area2:
    row = []
    for j in i:
        row.append(widen[j][0])
        row.append(widen[j][1])
    area.append(row)

for y in range(len(area)):
    for x in range(len(area[0])):
        if area[y][x]=="@":
            playerX = x
            playerY = y

def move2(x,y,direction,moving,data,cool,doit):
    if not cool:
        if moving == "[":
            if not move2(x+1,y,direction,"]",data,True,doit):
                return False
        else:
            if not move2(x-1,y,direction,"[",data,True,doit):
                return False
    if data[y+direction[1]][x+direction[0]] == ".":
        if doit:
            data[y+direction[1]][x+direction[0]] = moving
            data[y][x] = "."
        return True
    elif data[y+direction[1]][x+direction[0]] == "#":
        return False
    elif data[y+direction[1]][x+direction[0]] in "[]":
        if moving == "]" and direction==(-1,0):
            if doit:
                data[y+direction[1]][x+direction[0]] = moving
                data[y][x] = "."
            return True
        if moving == "[" and direction==(1,0):
            if doit:
                data[y+direction[1]][x+direction[0]] = moving
                data[y][x] = "."
            return True
        if move2(x+direction[0],y+direction[1],direction,data[y+direction[1]][x+direction[0]],data,False,doit):
            if doit:
                data[y+direction[1]][x+direction[0]] = moving
                data[y][x] = "."
            return True
    return False

for i in moves:
    if move2(playerX,playerY,dirs[i],"@",area,True,False):
        move2(playerX,playerY,dirs[i],"@",area,True,True)
        playerX+=dirs[i][0]
        playerY+=dirs[i][1]

for i in area:
    print("".join(i))

total = 0

for y in range(len(area)):
    for x in range(len(area[0])):
        if area[y][x]=="[":
            total+=y*100+x

print(total)
