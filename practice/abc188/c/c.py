#!/usr/bin/env python3
n = int(input())
players = list(map(int, input().split()))
winners = players

def round(players):
    winners = []
    for i in range(0, len(players), 2):
        player1 = players[i]
        player2 = players[i+1]
        if player1 > player2:
            winners.append(player1)
        else:
            winners.append(player2)
    return winners

# 決勝戦まで
for i in range(n - 1):
    winners = round(winners)

# 決勝戦
if winners[0] > winners[1]:
    print(players.index(winners[1]) + 1)
else:
    print(players.index(winners[0]) + 1)

## AC