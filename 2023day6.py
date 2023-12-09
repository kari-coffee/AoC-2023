# times = [int(i) for i in """53     89     76     98""".split()]
# dists = [int(i) for i in """313   1090   1214   1201""".split()]
# ans = 1
# for race in range(4):
#     t = times[race]
#     record = dists[race]
#     ways = 0
#     for charge in range(t):
#         if charge*(t-charge) > record:
#             ways += 1
#         else:
#             if ways > 1:
#                 break
#     ans *= ways
# print(ans)

# part 2

t = 53897698
record = 313109012141201
ways = 0
for charge in range(t):
    if charge*(t-charge) > record:
        ways += 1
    else:
        if ways > 1:
            break
print(ways)