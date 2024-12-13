data = """my input""".split("\n\n")

data = [i.split("\n") for i in data]

def sread(target,goal):
    index = target.find(goal)+len(goal)
    output = ""
    while target[index] in "0123456789":
        output+=target[index]
        index+=1
        if index==len(target):
            break
    return int(output)

claws = []
for i in data:
    claws.append(((sread(i[0],"X+"),sread(i[1],"X+")),(sread(i[0],"Y+"),sread(i[1],"Y+")),(sread(i[2],"X="),sread(i[2],"Y="))))
total = 0

for i in claws:
    Ax,Bx = i[0]
    Ay,By = i[1]
    Gx,Gy = i[2]
    numerA = Gx*By-Bx*Gy
    numerB = Ax*Gy-Gx*Ay
    denom = Ax*By-Bx*Ay
    if numerA%denom==0 and numerB%denom==0:
        total+=numerA//denom * 3
        total+=numerB//denom
print(total)
total = 0

for i in claws:
    Ax,Bx = i[0]
    Ay,By = i[1]
    Gx,Gy = i[2]
    Gx+=10000000000000
    Gy+=10000000000000
    numerA = Gx*By-Bx*Gy
    numerB = Ax*Gy-Gx*Ay
    denom = Ax*By-Bx*Ay
    if numerA%denom==0 and numerB%denom==0:
        total+=numerA//denom * 3
        total+=numerB//denom
print(total)
