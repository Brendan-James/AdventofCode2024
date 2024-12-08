def query(x,y,data):
    if not (0<=x<len(data[0]) and 0<=y<len(data)):
        return " "
    else:
        return data[y][x]

data = """my input""".split("\n")

data = [list(i) for i in data]
antinodes = {}

nodes = {}
for y in range(len(data)):
    for x in range(len(data[0])):
        if data[y][x]!=".":
            nodes[(x,y)] = data[y][x]

for i in nodes:
    for j in nodes:
        if i==j:
            continue
        if nodes[i]==nodes[j]:
            x = i[0]+(i[0]-j[0])
            y = i[1]+(i[1]-j[1])
            if query(x,y,data)!=" ":
                antinodes[(x,y)] = True

print(len(antinodes))

for i in nodes:
    for j in nodes:
        if i==j:
            continue
        if nodes[i]==nodes[j]:
            x = i[0]
            y = i[1]
            while query(x,y,data)!=" ":
                antinodes[(x,y)] = True
                x+=i[0]-j[0]
                y+=i[1]-j[1]

print(len(antinodes))

"""
for y in range(len(data)):
    output = ""
    for x in range(len(data[0])):
        if (x,y) in antinodes:
            output+="#"
        else:
            output+=data[y][x]
    print(output)
"""
