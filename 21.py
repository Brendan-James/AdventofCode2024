import itertools
import math

data = """my data""".split("\n")
keypad = {"7":(0,0),"8":(1,0),"9":(2,0),"4":(0,1),"5":(1,1),"6":(2,1),"1":(0,2),"2":(1,2),"3":(2,2),"X":(0,3),"0":(1,3),"A":(2,3)}
arrowpad = {"X":(0,0),"^":(1,0),"A":(2,0),"<":(0,1),"v":(1,1),">":(2,1)}

def code2keys(A,B,keys,scores):
    x1,y1 = keys[A]
    x2,y2 = keys[B]
    dx = x1-x2
    dy = y1-y2
    horiz = ""
    verti = ""
    if dx>0:
        horiz = "<"*dx
    if dx<0:
        horiz = ">"*abs(dx)
    if dy>0:
        verti = "^"*dy
    if dy<0:
        verti = "v"*abs(dy)
    options = list(set(itertools.permutations(horiz+verti,len(horiz+verti))))
    trueoptions = []
    for j in options:
        x = x1
        y = y1
        for k in j:
            x+=dirs[k][0]
            y+=dirs[k][1]
            if (x,y) == keys["X"]:
                break
        else:
            trueoptions.append(list(j)+["A"])
    minimum = math.inf
    for i in trueoptions:
        prev = "A"
        count = 0
        for j in i:
            count+=scores[(prev,j)]
            prev = j
        minimum = min(minimum,count)
    return minimum

scores = {}

for i in arrowpad:
    for j in arrowpad:
        scores[(i,j)] = 1
for x in range(2):
    newscores = {}
    for i in arrowpad:
        for j in arrowpad:
            newscores[(i,j)] = code2keys(i,j,arrowpad,scores)
    scores = newscores

newscores = {}
for i in keypad:
    for j in keypad:
        newscores[(i,j)] = code2keys(i,j,keypad,scores)
scores = newscores

total = 0

for i in data:
    prev = "A"
    count = 0
    for j in i:
        count+=scores[(prev,j)]
        prev = j
    total+= count * int(i[:-1])

print(total)

scores = {}

for i in arrowpad:
    for j in arrowpad:
        scores[(i,j)] = 1

for x in range(25):
    newscores = {}
    for i in arrowpad:
        for j in arrowpad:
            newscores[(i,j)] = code2keys(i,j,arrowpad,scores)
    scores = newscores

newscores = {}
for i in keypad:
    for j in keypad:
        newscores[(i,j)] = code2keys(i,j,keypad,scores)
scores = newscores

total = 0

for i in data:
    prev = "A"
    count = 0
    for j in i:
        count+=scores[(prev,j)]
        prev = j
    total+= count * int(i[:-1])
print(total)
