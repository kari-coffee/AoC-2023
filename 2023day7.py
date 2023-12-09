
# with open('input.txt') as f:
#     data = [line.strip().split() for line in f.readlines()]
#     hands = [line[0] for line in data]
#     bid = {line[0]:line[1] for line in data}

# def rank(hand):
#     h = {i:0 for i in hand}
#     for i in hand:
#         h[i] += 1
#     # five of a kind - 6
#     # four - 5
#     # full house - 4
#     # three - 3
#     # two pair - 2
#     # one pair - 1
#     # high card - 0
#     if 5 in h.values():
#         res = 6
#     elif 4 in h.values():
#         res = 5
#     elif 3 in h.values():
#         if 2 in h.values():
#             res = 4
#         else:
#             res = 3
#     elif list(h.values()).count(2) == 2:
#         res = 2
#     elif list(h.values()).count(2) == 1:
#         res = 1
#     else:
#         res = 0
#     return res

# convert = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':11,'Q':12,'K':13,'A':14}
# def compare(a, b):
#     ar = rank(a)
#     br = rank(b)
#     if ar > br:
#         return a
#     elif br > ar:
#         return b
#     elif ar == br:
#         for i in range(5):
#             ac = convert[a[i]]
#             bc = convert[b[i]]
#             if ac > bc:
#                 return a
#             elif ac < bc:
#                 return b 

# def partition(A, start, end):
#     x = A[end]
#     i = start-1
#     for j in range(start, end):
#         if compare(A[j], x) == x:
#             i += 1
#             temp = A[i]
#             A[i] = A[j]
#             A[j] = temp
#     temp = A[i+1]
#     A[i+1] = A[end]
#     A[end] = temp
#     return i+1

# def quicksort(A, start, end):
#     if start < end:
#         i = partition(A, start, end)
#         quicksort(A, start, i-1)
#         quicksort(A, i+1, end)

# quicksort(hands, 0, len(hands)-1)
# ans = 0
# for i in range(len(hands)):
#     ans += int(bid[hands[i]])*(i+1)
# print(ans)


#part 2
with open('input.txt') as f:
    data = [line.strip().split() for line in f.readlines()]
    hands = [line[0] for line in data]
    bid = {line[0]:line[1] for line in data}

def rank(hand):
    h = {i:0 for i in hand}
    for i in hand:
        h[i] += 1
    poss = [h]
    if 'J' in hand:
        for i in hand:
            if i != 'J':
                new = {k:v for k,v in h.items()}
                new['J'] = 0
                new[i] += h['J']
                if new not in poss:
                    poss.append(new)
    # five of a kind - 6
    # four - 5
    # full house - 4
    # three - 3
    # two pair - 2
    # one pair - 1
    # high card - 0
    ans = 0
    for p in poss:
        if 5 in p.values():
            res = 6
        elif 4 in p.values():
            res = 5
        elif 3 in p.values():
            if 2 in p.values():
                res = 4
            else:
                res = 3
        elif list(p.values()).count(2) == 2:
            res = 2
        elif list(p.values()).count(2) == 1:
            res = 1
        else:
            res = 0
        ans = max(ans, res)
    return ans

convert = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':1,'Q':12,'K':13,'A':14}
def compare(a, b):
    ar = rank(a)
    br = rank(b)
    if ar > br:
        return a
    elif br > ar:
        return b
    elif ar == br:
        for i in range(5):
            ac = convert[a[i]]
            bc = convert[b[i]]
            if ac > bc:
                return a
            elif ac < bc:
                return b 

def partition(A, start, end):
    x = A[end]
    i = start-1
    for j in range(start, end):
        if compare(A[j], x) == x:
            i += 1
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
    temp = A[i+1]
    A[i+1] = A[end]
    A[end] = temp
    return i+1

def quicksort(A, start, end):
    if start < end:
        i = partition(A, start, end)
        quicksort(A, start, i-1)
        quicksort(A, i+1, end)

quicksort(hands, 0, len(hands)-1)
ans = 0
for i in range(len(hands)):
    ans += int(bid[hands[i]])*(i+1)
print(ans)
