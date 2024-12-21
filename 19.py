from functools import cache

options = "my input".split(", ")

data = """my input""".split("\n")

@cache
def constructable(pattern):
    global options
    if pattern in options:
        return True
    for i in options:
        if pattern[:len(i)] == i:
            if constructable(pattern[len(i):]):
                return True
    return False

count = 0
total = 0

@cache 
def countstruct(pattern):
    global options
    if len(pattern) == 0:
        return 1
    if not constructable(pattern):
        return 0
    total = 0
    for i in options:
        if pattern[:len(i)] == i:
            total += countstruct(pattern[len(i):])
    return total


for i in data:
    if constructable(i):
        count+=1
        total+=countstruct(i)

print(count,total)
