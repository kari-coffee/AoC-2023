# with open('input.txt') as f:
#     data = [line.strip() for line in f.readlines()]
#     ans = 0
#     for line in data:
#         s = ''
#         for j in line:
#             if j.isdigit():
#                 s += j
#                 break
#         for j in range(len(line)-1, -1, -1):
#             if line[j].isdigit():
#                 s += line[j]
#                 break
#         ans += int(s)
#     print(ans)

# part 2
digits = {'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'zero':0}
with open('input.txt') as f:
    data = [line.strip() for line in f.readlines()]
    ans = 0
    for line in data:
        a = ''
        b = ''
        s = ''
        stop = False
        for i in range(len(line)):
            if line[i].isdigit():
                a = line[i]
                break
            s += line[i]
            for j in digits:
                if j in s:
                    a = str(digits[j])
                    stop = True
                    break
            if stop:
                break
        s = ''
        stop = False
        for i in range(len(line)-1, -1, -1):
            if line[i].isdigit():
                b = line[i]
                break
            s += line[i]
            for j in digits:
                if j in s[::-1]:
                    b = str(digits[j])
                    stop = True
                    break
            if stop:
                break
        ans += int(a+b)
    print(ans)