with open('input2.txt') as f:
    data = [[int(i) for i in line.strip().split()] for line in f.readlines()]

def diff(hist):
    d = [hist[i+1]-hist[i] for i in range(len(hist)-1)]
    return d

# def extrapolate(hist):
#     prev = diff(hist)
#     if len(set(prev)) == 1:
#         return hist[-1]+prev[0]
#     return hist[-1]+extrapolate(prev)

# ans = 0
# for hist in data:
#     ans += extrapolate(hist)
# print(ans)

# part 2
def extrapolate_back(hist):
    prev = diff(hist)
    if len(set(prev)) == 1:
        return hist[0]-prev[0]
    return hist[0]-extrapolate_back(prev)

ans = 0
for hist in data:
    ans += extrapolate_back(hist)
print(ans)