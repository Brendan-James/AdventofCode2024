data = """my input""".split("\n")

data = [i.split(" ") for i in data]
data = [[int(i) for i in j] for j in data]

count = 0

for i in data:
    if i[0]<i[1]:
        for j in range(len(i)-1):
            if i[j]<i[j+1] and 1<=i[j+1]-i[j]<=3:
                continue
            else:
                break
        else:
            count+=1
    else:
        for j in range(len(i)-1):
            if i[j+1]<i[j] and 1<=i[j]-i[j+1]<=3:
                continue
            else:
                break
        else:
            count+=1

print(count)
count = 0

for row in data:
    i = row
    if i[0]<i[1]:
        for j in range(len(i)-1):
            if i[j]<i[j+1] and 1<=i[j+1]-i[j]<=3:
                continue
            else:
                break
        else:
            count+=1
            continue
    else:
        for j in range(len(i)-1):
            if i[j+1]<i[j] and 1<=i[j]-i[j+1]<=3:
                continue
            else:
                break
        else:
            count+=1
            continue
    for skip in range(len(row)):
        i = row[:skip]+row[skip+1:]
        print(row,i)
        if i[0]<i[1]:
            for j in range(len(i)-1):
                if i[j]<i[j+1] and 1<=i[j+1]-i[j]<=3:
                    continue
                else:
                    break
            else:
                count+=1
                break
        else:
            for j in range(len(i)-1):
                if i[j+1]<i[j] and 1<=i[j]-i[j+1]<=3:
                    continue
                else:
                    break
            else:
                count+=1
                break
print(count)
