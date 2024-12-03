data = """my input"""


# the right strategy is probably regular expressions or something but this was the first thought I had so I implemented it
step = 0
a = 0
b = 0
digits = "0123456789"
total = 0
for i in data:
    if i == "m":
        step = 1
        a = 0
        b = 0
    elif step == 1 and i=="u":
        step = 2
    elif step == 2 and i=="l":
        step = 3
    elif step == 3 and i=="(":
        step = 4
    elif step == 4 and i in digits:
        a*=10
        a+=int(i)
    elif step == 4 and i==",":
        step = 5
    elif step == 5 and i in digits:
        b*=10
        b+=int(i)
    elif step == 5 and i==")":
        total+=a*b
        step = 0
    else:
        step = 0

print(total)

do = 0
actually = True
step = 0
a = 0
b = 0
total = 0
for i in data:
    if i == "m" and actually:
        step = 1
        a = 0
        b = 0
    elif step == 1 and i=="u":
        step = 2
    elif step == 2 and i=="l":
        step = 3
    elif step == 3 and i=="(":
        step = 4
    elif step == 4 and i in digits:
        a*=10
        a+=int(i)
    elif step == 4 and i==",":
        step = 5
    elif step == 5 and i in digits:
        b*=10
        b+=int(i)
    elif step == 5 and i==")":
        total+=a*b
        step = 0
    else:
        step = 0
    if i=="d":
        do = 1
    elif do==1 and i=="o":
        do = 2
    elif do==2 and i=="(":
        do = 3
    elif do==3 and i==")":
        actually = True
        do = 0
    elif do==2 and i=="n":
        do = 4
    elif do==4 and i=="'":
        do = 5
    elif do==5 and i=="t":
        do = 6
    elif do==6 and i=="(":
        do = 7
    elif do==7 and i==")":
        actually = False
        do = 0
    else:
        do = 0
print(total)
