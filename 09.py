import copy
def query(x,y,data):
    if not (0<=x<len(data[0]) and 0<=y<len(data)):
        return " "
    else:
        return data[y][x]

data = list("my input")


data = [int(i) for i in data]

blockus = []

for i,v in enumerate(data):
    if i%2==1:
        for n in range(v):
            blockus.append(".")
    else:
        for n in range(v):
            blockus.append(i//2)
index = 0

while index<len(blockus):
    if blockus[index]!=".":
        index+=1
        continue
    current = blockus.pop()
    if index<len(blockus):
        blockus[index] = current

total = 0
for i,v in enumerate(blockus):
    total+=i*v

print(total)

blockus = []

for i,v in enumerate(data):
    if i%2==1:
        blockus.append((v,"."))
    else:
        blockus.append((v,i//2))

index = len(blockus)-1
while index>0:
    if blockus[index][1]==".":
        if index==len(blockus)-1 or blockus[index][0]==0:
            blockus.pop(index)
        index-=1
        continue
    size = blockus[index][0]
    for i,v in enumerate(blockus):
        if v[1]!=".":
            continue
        if i>=index:
            index-=1
            break
        if v[0]>=size:
            blockus[i] = (v[0]-size,".")
            blockus.insert(i,(blockus[index][0],blockus[index][1]))
            blockus[index+1] = (blockus[index+1][0],".")
            break
    else:
        index-=1

total = 0
count = 0
for i in blockus:
    for j in range(i[0]):
        if i[1]!=".":
            total+=count*i[1]
        count+=1

print(total)
