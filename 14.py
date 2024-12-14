from collections import defaultdict

data = """my input""".split("\n")

width = 101
height = 103

data = [i.split(" ") for i in data]

def sread(target,goal):
    index = target.find(goal)+len(goal)
    output = ""
    while target[index] in "-0123456789":
        output+=target[index]
        index+=1
        if index==len(target):
            break
    return int(output)

bots = []
for i in data:
    bots.append(((sread(i[0],"p="),sread(i[0],",")),(sread(i[1],"v="),sread(i[1],","))))

quads = [0,0,0,0]

for i in bots:
    x = i[0][0]
    y = i[0][1]
    dx = i[1][0]
    dy = i[1][1]
    x=(x+dx*100)%width
    y=(y+dy*100)%height
    quad = 0
    if x==(width-1)//2 or y==(height-1)//2:
        continue
    if x>(width-1)//2:
        quad+=1
    if y>(height-1)//2:
        quad+=2
    quads[quad]+=1

result = 1
for i in quads:
    result*=i
print(result)
steps = 0
while True:
    steps+=1
    newbots = []
    current = defaultdict(int)

    for i in bots:
        x = i[0][0]
        y = i[0][1]
        dx = i[1][0]
        dy = i[1][1]
        x=(x+dx)%width
        y=(y+dy)%height
        current[(x,y)]+=1
        newbots.append(((x,y),(dx,dy)))
    bots = newbots
    for i in current:
        if current[i]!=1:
            break
    else:
        for y in range(height):
            row = ""
            for x in range(width):
                if (x,y) in current:
                    row+=str(current[(x,y)]%10)
                else:
                    row+="."
            print(row)
        print(steps)
        break
