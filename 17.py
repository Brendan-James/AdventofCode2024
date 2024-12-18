rA = "my input"
rB = "my input"
rC = "my input"

data = ["my input"]

def process(rA,rB,rC,data):
    ip = 0
    output = []
    while ip<len(data):
        operator = data[ip]
        L_op = data[ip+1]
        C_op = data[ip+1]
        if L_op == 4:
            C_op = rA
        elif L_op==5:
            C_op = rB
        elif L_op==6:
            C_op = rC
        if operator == 0:
            rA = rA//(2**C_op)
            ip+=2
        elif operator==1:
            rB = rB^L_op
            ip+=2
        elif operator==2:
            rB = C_op%8
            ip+=2
        elif operator==3:
            if rA==0:
                ip+=2
            else:
                ip = L_op
        elif operator==4:
            rB = rB^rC
            ip+=2
        elif operator==5:
            output.append(C_op%8)
            ip+=2
        elif operator == 6:
            rB = rA//(2**C_op)
            ip+=2
        elif operator == 7:
            rC = rA//(2**C_op)
            ip+=2
    return output

print(",".join([str(i) for i in process(rA,rB,rC,data)]))

rA = 8**(len(data)-1)

result = process(rA,rB,rC,data)

while result != data:
    for i in reversed(range(len(data))):
        if data[i]!=result[i]:
            rA+=8**i
            increments[i]+=1
            break
    result = process(rA,rB,rC,data)

print(rA,",".join([str(i) for i in process(rA,rB,rC,data)]))
print(increments)
