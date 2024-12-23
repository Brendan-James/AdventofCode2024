from functools import cache

data = """my input""".split("\n")

@cache
def step(num):
    num = ((num*64)^num)%16777216
    num = ((num//32)^num)%16777216
    num = ((num*2048)^num)%16777216
    return num

total = 0
for i in data:
    num = int(i)
    for j in range(2000):
        num = step(num)
    total+=num
print(total)

best = defaultdict(int)

for i in data:
    num = int(i)
    prev = num%10
    window = []
    seen = {}
    for j in range(2000):
        num = step(num)
        window.append(num%10-prev)
        prev = num%10
        if len(window) == 5:
            window.pop(0)
        if len(window) == 4:
            if tuple(window) not in seen:
                seen[tuple(window)] = prev
    for j in seen:
        best[j] += seen[j]

total = 0

for i in best:
    total = max(total,best[i])

print(total)
