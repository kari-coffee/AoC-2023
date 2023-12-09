sequence = """LRLRRRLRLLRRLRLRRRLRLRRLRRLLRLRRLRRLRRRLRRRLRLRRRLRLRRLRRLLRLRLLLLLRLRLRRLLRRRLLLRLLLRRLLLLLRLLLRLRRLRRLRRRLRRRLRRLRRLRRRLRLRLRRLRLRLRLRRLRRRLLRLLRRLRLRRRLRLRRRLRLRRRLRRRLRRLRLLLLRLRRRLRLRRLRLRRLRRLRRLLRRRLLLLLLRLRRRLRRLLRRRLRRLLLRLRLRLRRRLRRLRLRRRLRRLRRRLLRRLRRLLLRRRR"""

# (for both parts)
g = {}
with open('input.txt') as f:
    data = f.readlines()
    for line in data:
        a, b = line.split(" = ")
        l, r = b[1:-2].split(', ')
        g[a] = (l, r)

# cur = 'AAA'
# i = 0
# while cur != 'ZZZ':
#     if sequence[i%len(sequence)] == 'L':
#         j = 0
#     else:
#         j = 1
#     cur = g[cur][j]
#     i += 1
# print(i)

# part 2
from math import lcm
sequence = [0 if l == 'L' else 1 for l in sequence]
starts = [node for node in g if node[-1] == 'A']
i = 0
ends_with_z = set(node for node in g if node[-1] == 'Z')

def path_length(cur):
    i = 0
    while True:
        j = sequence[i%len(sequence)]
        cur = g[cur][j]
        i += 1
        if cur in ends_with_z:
            return i

paths = []
for cur in starts:
    paths.append(path_length(cur))

x = paths[0]
for y in paths[1:]:
    x = lcm(x, y)
print(x)