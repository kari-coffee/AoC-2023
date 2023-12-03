# import re
# with open('input.txt') as f:
#     data = f.readlines()
#     ans = 0
#     rgb = [12, 13, 14]
#     for line in data:
#         valid = True
#         for subset in line[line.index(': '):].split(';'):
#             line_rgb = [re.findall("\d+ red", subset), re.findall("\d+ green", subset), re.findall("\d+ blue", subset)]
#             line_rgb = [0 if i == [] else int(i[0].split()[0]) for i in line_rgb]
            
#             for i in range(3):
#                 if line_rgb[i] > rgb[i]:
#                     valid = False
#         if valid:
#             ans += int(line[line.index('Game ')+5:line.index(':')])
#     print(ans)

#part 2
import re
from operator import mul
from functools import reduce
with open('input.txt') as f:
    data = f.readlines()
    ans = 0
    for line in data:
        max_rgb = [0, 0, 0]
        for subset in line[line.index(': '):].split(';'):
            line_rgb = [re.findall("\d+ red", subset), re.findall("\d+ green", subset), re.findall("\d+ blue", subset)]
            line_rgb = [0 if i == [] else int(i[0].split()[0]) for i in line_rgb]
            
            for i in range(3):
                max_rgb[i] = max(max_rgb[i], line_rgb[i])
        ans += reduce(mul, max_rgb)
    print(ans)