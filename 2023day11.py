# greedy method for part 1 (as in can't be reused for part 2)
# with open('input.txt') as f:
#     data = [list(line.strip()) for line in f.readlines()]
# # expand rows
# new = []
# for row in data:
#     if len(set(row)) == 1 and row[0] == '.':
#         new.append(['.' for i in range(len(row))])
#         new.append(['.' for i in range(len(row))])
#     else:
#         new.append(row)

# # expand cols
# space = []
# new = [[new[y][x] for y in range(len(new))] for x in range(len(new[0]))] # flip grid
# for row in new:
#     if len(set(row)) == 1 and row[0] == '.':
#         space.append(['.' for i in range(len(row))])
#         space.append(['.' for i in range(len(row))])
#     else:
#         space.append(row)
# space = [[space[y][x] for y in range(len(space))] for x in range(len(space[0]))] # flip back

# galaxies = []
# for y in range(len(space)):
#     for x in range(len(space[0])):
#         if space[y][x] == '#':
#             galaxies.append((y, x))
# ans = 0
# for g in galaxies:
#     for g2 in galaxies:
#         if g != g2:
#             ans += (abs(g2[1]-g[1])+abs(g2[0]-g[0]))
# print(ans//2)

# part 2
with open('input.txt') as f:
    data = [list(line.strip()) for line in f.readlines()]
# expand rows
new = []
for row in data:
    if len(set(row)) == 1 and row[0] == '.':
        new.append(['X' for i in range(len(row))])
    else:
        new.append(row)
# expand cols
space = []
new = [[new[y][x] for y in range(len(new))] for x in range(len(new[0]))] # flip grid
for row in new:
    if len(set(row)) == 2 and '.' in row and 'X' in row:
        space.append(['X' for i in range(len(row))])
    else:
        space.append(row)
space = [[space[y][x] for y in range(len(space))] for x in range(len(space[0]))] # flip back

galaxies = []
for y in range(len(space)):
    for x in range(len(space[0])):
        if space[y][x] == '#':
            galaxies.append((y, x))
def dist(a, b):
    loy = min(a[0], b[0])
    hiy = max(a[0], b[0])
    lox = min(a[1], b[1])
    hix = max(a[1], b[1])
    res = 0
    for y in range(loy, hiy):
        if space[y][hix] == 'X':
            res += 1_000_000
        else:
            res += 1
    for x in range(lox, hix):
        if space[loy][x] == 'X':
            res += 1_000_000
        else:
            res += 1
    return res
ans = 0
done = set()
for g in galaxies:
    for g2 in galaxies:
        if g != g2 and (g, g2) not in done and (g2, g) not in done:
            ans += dist(g, g2)
            done.add((g, g2))
print(ans)
