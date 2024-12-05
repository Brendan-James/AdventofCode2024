from functools import cmp_to_key
orders="""my input pt.1""".split("\n")

updates = """my input pt.2""".split("\n")

orders = [i.split("|") for i in orders]
updates = [i.split(",") for i in updates]

def compare(A,B):
    for i in orders:
        if A in i and B in i:
            return -1 if i[0]==A else 1
    return 0

total1 = 0
total2 = 0

for i in updates:
    s = sorted(i,key=cmp_to_key(compare))
    if i==s:
        total1+=int(i[len(i)//2])
    else:
        total2+=int(i[len(i)//2])

print(total1)
print(total2)
