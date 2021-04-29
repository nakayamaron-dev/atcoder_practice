#!/usr/bin/env python3

# トーナメントの再帰関数
def round(players):
    
    # インナー関数
    def _round(players):
        winners = []

        # 決勝戦は敗者を返す。
        if len(players) == 2:
            return min(players)

        # 決勝戦以外は勝者をwinnersに追加。
        for i in range(1, len(players), 2):
            winner = max(players[i-1], players[i])
            winners.append(winner)

        return _round(winners)

    return _round(players)

def solve():
    N = int(input())
    A = list(map(int, input().split()))

    runner_up = round(A)

    return A.index(runner_up) + 1

print(solve())

# self AC
