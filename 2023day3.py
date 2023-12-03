# with open('input.txt') as f:
#     data = [list(line.strip()) for line in f.readlines()]
#     ans = 0
#     coords = [] # [[number as string, starting coord]]
#     for i in range(len(data)):
#         cur = ''
#         start_coord = [i, 0]
#         for j in range(len(data[i])):
#             if not data[i][j].isdigit():
#                 if cur != '':
#                     coords.append([cur, start_coord])
#                     cur = ''
#                 start_coord = [i, j+1]
#             else:
#                 cur += data[i][j]
#         if cur != '':
#             coords.append([cur, start_coord])
                
#     for s, c in coords:
#         # c = [y, x]
#         y = c[0]
#         done = False
#         for x in range(c[1], c[1]+len(s)):
#             for dy, dx in ((0, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 0), (1, 1)):
#                 if 0 <= y+dy < len(data) and 0 <= x+dx < len(data[0]):
#                     if data[y+dy][x+dx] not in '0123456789.':
#                         ans += int(s)
#                         done = True
#                         break
#             if done:
#                 break
#     print(ans)

# part 2
with open('input.txt') as f:
    data = [list(line.strip()) for line in f.readlines()]
    ans = 0
    coords = [] # [[number as string, starting coord]]
    for i in range(len(data)):
        cur = ''
        start_coord = [i, 0]
        for j in range(len(data[i])):
            if not data[i][j].isdigit():
                if cur != '':
                    coords.append([cur, start_coord])
                    cur = ''
                start_coord = [i, j+1]
            else:
                cur += data[i][j]
        if cur != '':
            coords.append([cur, start_coord])
                
    gears = {}
    for s, c in coords:
        # c = [y, x]
        y = c[0]
        done = False
        for x in range(c[1], c[1]+len(s)):
            for dy, dx in ((0, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 0), (1, 1)):
                if 0 <= y+dy < len(data) and 0 <= x+dx < len(data[0]):
                    if data[y+dy][x+dx] == '*':
                        if (y+dy, x+dx) in gears:
                            if int(s) not in gears[(y+dy, x+dx)]:
                                gears[(y+dy, x+dx)].append((int(s)))
                        else:
                            gears[(y+dy, x+dx)] = [int(s)]
    for i in gears:
        if len(gears[i]) == 2:
            ans += gears[i][0]*gears[i][1]
    print(ans)