# with open('input.txt') as f:
#     points = 0
#     data = f.readlines()
#     for line in data:
#         line = line[line.index(': ')+2:]
#         winning, have = line.split(' | ')
#         winning = [int(n.strip()) for n in winning.split()]
#         have = [int(n.strip()) for n in have.split()]
#         card = 0
#         for i in have:
#             if i in winning:
#                 if card == 0:
#                     card = 1
#                 else:
#                     card *= 2
#         points += card
#     print(points)

# part 2
with open('input.txt') as f:
    data = f.readlines()
    cards = {i:0 for i in range(1, len(data)+1)}
    total = 0
    wins = {} # dictionary mapping card to the cards it wins
    for line in data:
        ix = int(line[5:line.index(':')])
        line = line[line.index(': ')+2:]
        winning, have = line.split(' | ')
        winning = [int(n.strip()) for n in winning.split()]
        have = [int(n.strip()) for n in have.split()]

        w = 0
        for i in have:
            if i in winning:
                w += 1

        wins[ix] = [i for i in range(ix+1, ix+w+1)]
        cards[ix] += 1
        for i in wins[ix]:
            cards[i] += cards[ix]
    print(sum(cards.values()))