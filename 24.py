data = """my input""".split("\n")

gates = """my input""".split("\n")

gates = [i.split(" -> ") for i in gates]
gates = [[i[0].split(" "),i[1]] for i in gates]

for a,b in gates:
    a[0],a[2] = sorted([a[0],a[2]])


data = [i.split(": ") for i in data]
def run(data,gates):
    facts = {}

    for i in data:
        facts[i[0]] = (i[1]=="1")

    while len(gates)>0:
        newgates = []
        for i in gates:
            if not (i[0][0] in facts and i[0][2] in facts):
                newgates.append(i)
                continue
            else:
                if i[0][1]=="AND":
                    facts[i[1]] = (facts[i[0][0]] and facts[i[0][2]])
                elif i[0][1]=="OR":
                    facts[i[1]] = (facts[i[0][0]] or facts[i[0][2]])
                elif i[0][1]=="XOR":
                    facts[i[1]] = (facts[i[0][0]] != facts[i[0][2]])
        gates = newgates
    return facts


def process(num,letter):
    out = str(num)
    while len(out)<2:
        out = "0"+out
    return letter+out

def calculate(facts,letter):
    index = 0
    total = 0
    while process(index,letter) in facts:
        if facts[process(index,letter)]:
            total+=2**index
        index+=1
    return total

print(calculate(run(data,gates),"z"))

# I did a lot of manual work for this one

swaps = {"z11":"wpd","skh":"jqf","mdd":"z19","z37":"wts"}
newswaps = {}

for i in swaps:
    newswaps[swaps[i]] = i
    newswaps[i] = swaps[i]

swaps = newswaps

newgates = {}
for i in gates:
    if i[1] in swaps:
        newgates[tuple(i[0])] = swaps[i[1]]
    else:
        newgates[tuple(i[0])] = i[1]

gates = newgates

andies = []
xories = []

for i in range(44):
    andies.append(gates[(process(i,"x"),"AND",process(i,"y"))])
    xories.append(gates[(process(i,"x"),"XOR",process(i,"y"))])

carries = ["hjp"]
As = ["???"]
outs = []

for i in range(1,44):
    # THE FULL ADDER SYSTEM
    # carry AND xorie -> A
    # carry XOR xorie -> output
    # andie OR A -> carry
    carry = carries[i-1]
    a1,a2 = sorted([carry,xories[i]])
    if (a1,"AND",a2) not in gates:
        print(i,"no AND",a1,a2)
    else:
        As.append(gates[(a1,"AND",a2)])
        outs.append(gates[(a1,"XOR",a2)])
    b1,b2 = sorted([As[i],andies[i]])
    if (b1,"OR",b2) not in gates:
        print(i,"no OR")
        print(As[i])
        print(andies[i])
    else:
        carries.append(gates[(b1,"OR",b2)])

print(outs)

print(",".join(sorted([i for i in swaps])))
