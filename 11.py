data = """my input""".split(" ")

stones = [int(i) for i in data]

def process(stones):
    newstones = []
    for i in stones:
        if i==0:
            newstones.append(1)
        elif len(str(i))%2==0:
            newstones.append(int(str(i)[:len(str(i))//2]))
            newstones.append(int(str(i)[len(str(i))//2:]))
        else:
            newstones.append(i*2024)
    return newstones


for i in range(25):
    stones = process(stones)

print(len(stones))

newstones = {}

for i in stones:
    if i not in newstones:
        newstones[i]=0
    newstones[i]+=1

stones = newstones

def process2(stones):
    newstones = {}
    for i in stones:
        if i==0:
            if 1 not in newstones:
                newstones[1] = 0
            newstones[1] += stones[0]
        elif len(str(i))%2==0:
            if int(str(i)[:len(str(i))//2]) not in newstones:
                newstones[int(str(i)[:len(str(i))//2])] = 0
            if int(str(i)[len(str(i))//2:]) not in newstones:
                newstones[int(str(i)[len(str(i))//2:])] = 0
            newstones[int(str(i)[:len(str(i))//2])]+=stones[i]
            newstones[int(str(i)[len(str(i))//2:])]+=stones[i]
        else:
            if i*2024 not in newstones:
                newstones[i*2024] = 0
            newstones[i*2024]+=stones[i]
    return newstones

for i in range(50):
    stones = process2(stones)

print(sum([stones[i] for i in stones]))
